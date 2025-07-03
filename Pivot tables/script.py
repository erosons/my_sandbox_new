sqlCommand ="""
SET NOCOUNT ON

if OBJECT_ID('tempdb..#lifecycle_status') is not null
drop table #lifecycle_status;

create table #lifecycle_status
(LDC_ACCT_ID numeric(15, 0),
LIFECYCLE_STATUS varchar(32));

insert into #lifecycle_status
select LA.LDC_ACCT_ID, '01 Processing'
from LDC_ACCOUNT LA
where nullif(LA.END_DT, 0) is null and LA.STATUS_CD in ('PEND', 'NEW');

insert into #lifecycle_status
select LA.LDC_ACCT_ID, '02 Utility Reject'
from LDC_ACCOUNT LA
where LA.STATUS_CD = 'ENRJ';

insert into #lifecycle_status
select LA.LDC_ACCT_ID, '03 Ops Reject'
from LDC_ACCOUNT LA
where LA.STATUS_CD in ('DUP', 'CFWD');

insert into #lifecycle_status
select LA.LDC_ACCT_ID, '09 Collections'
from LDC_ACCOUNT LA
where LA.STATUS_CD = 'CRMS';

insert into #lifecycle_status
select LA.LDC_ACCT_ID, '04 Cancelled'
from LDC_ACCOUNT LA
where
(LA.STATUS_CD = 'CNCL'
or (LA.STATUS_CD in ('PEFI', 'CNCL') and nullif(LA.START_DT, 0) = nullif(LA.END_DT, 0))
or (LA.STATUS_CD = 'PEFI' and nullif(LA.END_DT, 0) IS NULL)
or (nullif(LA.END_DT, 0) IS not NULL and nullif(LA.END_DT, 0) < nullif(LA.START_DT, 0))
or (nullif(LA.END_DT, 0) IS not NULL and nullif(LA.START_DT, 0) IS NULL))
and LA.LDC_ACCT_ID not in (select LDC_ACCT_ID from #lifecycle_status);

insert into #lifecycle_status
select LA.LDC_ACCT_ID, '05 Pending Flow Start'
from LDC_ACCOUNT LA
where
(LA.STATUS_CD = 'ENRL'
or ((convert(datetime, (convert(varchar(8), nullif(LA.START_DT, 0))), 113) > GETDATE()
and nullif(LA.END_DT, 0) IS NULL) and LA.STATUS_CD not in ('PEFI', 'TERM','FIN')))
and LA.LDC_ACCT_ID not in (select LDC_ACCT_ID from #lifecycle_status);

insert into #lifecycle_status
select LA.LDC_ACCT_ID, '06 Active On Flow'
from LDC_ACCOUNT LA
where
(convert(datetime, (convert(varchar(8), nullif(LA.START_DT, 0))), 113) <= GETDATE()
and nullif(LA.END_DT, 0) is null
and LA.STATUS_CD not in ('PEFI', 'TERM','FIN'))
and LA.LDC_ACCT_ID not in (select LDC_ACCT_ID from #lifecycle_status);

insert into #lifecycle_status
select LA.LDC_ACCT_ID, '07 Pending Flow Stop'
from LDC_ACCOUNT LA
where
((convert(datetime, (convert(varchar(8), nullif(LA.START_DT, 0))), 113) <= GETDATE()
and convert(datetime, (convert(varchar(8), nullif(LA.END_DT, 0))), 113) > GETDATE())
or (LA.STATUS_CD = 'PEFI' and convert(datetime, (convert(varchar(8), nullif(LA.END_DT, 0))), 113) > GETDATE()))
and LA.LDC_ACCT_ID not in (select LDC_ACCT_ID from #lifecycle_status);

insert into #lifecycle_status
select LA.LDC_ACCT_ID, '08 Inactive Off Flow'
from LDC_ACCOUNT LA
where
((LA.STATUS_CD in ('TERM','FIN') and nullif(LA.END_DT, 0) is null)
or (convert(datetime, (convert(varchar(8), nullif(LA.START_DT, 0))), 113) <= GETDATE()
and nullif(LA.END_DT, 0) is not null
and convert(datetime, (convert(varchar(8), nullif(LA.END_DT, 0))), 113) <= GETDATE()))
and LA.LDC_ACCT_ID not in (select LDC_ACCT_ID from #lifecycle_status);

insert into #lifecycle_status
select LA.LDC_ACCT_ID, '10 Status Error'
from LDC_ACCOUNT LA
where LA.LDC_ACCT_ID not in (select LDC_ACCT_ID from #lifecycle_status);

IF OBJECT_ID(N'tempdb..##ldccontacts ', N'U') IS NOT NULL
DROP TABLE ##ldccontacts

select a.ACCT_ID, c.ADDR_ID, LAST_NM, FIRST_NM,  PHONE_NO, EMAIL_ADDR_TX, c.CONTACT_TY_CD,  l.LDC_ACCT_ID,
ROW_NUMBER() over (PARTITION BY l.LDC_ACCT_ID  order by c.SYS_TM_STAMP desc) as ROW
into ##ldccontacts
from test..CONTACT c
join test..LDC_ACCOUNT l on l.LDC_ACCT_ID = c.RELATE_ID and CLASS_NM = 'cLDCAccount'
join test..ACCOUNT a on a.ACCT_ID = l.ACCT_ID
--join test.dbo.[ADDRESS] addr on l.ADDR_ID = addr.ADDR_ID
--	and  c.ADDR_ID = addr.ADDR_ID
;


IF OBJECT_ID(N'tempdb..##acctcontacts ', N'U') IS NOT NULL
DROP TABLE ##acctcontacts

select a.ACCT_ID, c.ADDR_ID, LAST_NM, FIRST_NM,  PHONE_NO, EMAIL_ADDR_TX, c.CONTACT_TY_CD,
ROW_NUMBER() over (PARTITION BY a.ACCT_ID  order by c.SYS_TM_STAMP desc) as ROW
into ##acctcontacts
from test..CONTACT c
join test..ACCOUNT a on a.ACCT_ID = c.RELATE_ID and CLASS_NM = 'cAccount'
--join test.dbo.[ADDRESS] addr on l.ADDR_ID = addr.ADDR_ID
--	and  c.ADDR_ID = addr.ADDR_ID
;

IF OBJECT_ID(N'tempdb..##ldccontracts ', N'U') IS NOT NULL
DROP TABLE ##ldccontracts

Select
LA.LDC_ACCT_ID
, A.ACCT_ID
, coalesce(convert(char(10), convert(date, (convert(varchar(8), nullif(LC.START_DT, 0))), 113)),'') AS START_DT
, coalesce(convert(char(10), convert(date, (convert(varchar(8), nullif(LC.END_DT, 0))), 113)),'')AS END_DT
, LC.SYS_TM_STAMP
, ROW_NUMBER() over (PARTITION BY LC.LDC_ACCT_ID  order by LC.SYS_TM_STAMP desc) as ROW
into ##ldccontracts
FROM
test..LDC_ACCOUNT LA
JOIN test..ACCOUNT A ON LA.ACCT_ID = A.ACCT_ID
JOIN test..LDC_CONTRACT LC ON LA.LDC_ACCT_ID = LC.LDC_ACCT_ID

;

-- *** Something Jim Cargle programmed, not exactly sure what it does ***
--Jim took the latest record for these particular fields so that he didn't have to build it into the query and could just call it as a table.

WITH
rate_grp as (select LDC_ACCT_ID, START_DT, END_DT, RATE_CD, SERVICE_TY_CD,
ROW_NUMBER() over (partition by LDC_ACCT_ID order by START_DT desc) as ROW
from RATING_GROUP),

meter as (select RELATE_ID, START_DT, METER_NO,
ROW_NUMBER() over (partition by RELATE_ID order by START_DT desc) as ROW
from test..METER),
pindexval as (select PRICE_INDEX_ID, VALUE_NO,
ROW_NUMBER() over (partition by PRICE_INDEX_ID order by START_DT desc) as ROW
from test.dbo.PRICE_INDEX_VALUE),
MM_Channel as (SELECT RELATED_ID, VALUE_TX,
ROW_NUMBER() over (PARTITION BY RELATED_ID order by SYS_TM_STAMP desc) as ROW
FROM test.dbo.USER_FIELD_DATA
WHERE FIELD_DEF_ID = 292),
MM_Broker as (SELECT RELATED_ID, VALUE_TX,
ROW_NUMBER() over (PARTITION BY RELATED_ID order by SYS_TM_STAMP desc) as ROW
FROM test.dbo.USER_FIELD_DATA
WHERE FIELD_DEF_ID = 293),
MM_Agent as (SELECT RELATED_ID, VALUE_TX,
ROW_NUMBER() over (PARTITION BY RELATED_ID order by SYS_TM_STAMP desc) as ROW
FROM test.dbo.USER_FIELD_DATA
WHERE FIELD_DEF_ID = 294),
Verification_ID as (SELECT RELATED_ID, VALUE_TX,
ROW_NUMBER() over (PARTITION BY RELATED_ID order by SYS_TM_STAMP desc) as ROW
FROM test.dbo.USER_FIELD_DATA
WHERE FIELD_DEF_ID = 295),
Fixedpct as (SELECT RELATED_ID, VALUE_TX,
ROW_NUMBER() over (PARTITION BY RELATED_ID order by SYS_TM_STAMP desc) as ROW
FROM test.dbo.USER_FIELD_DATA
WHERE FIELD_DEF_ID = 356),
MM_Commission as (SELECT RELATED_ID, VALUE_TX,
ROW_NUMBER() over (PARTITION BY RELATED_ID order by SYS_TM_STAMP desc) as ROW
FROM test.dbo.USER_FIELD_DATA
WHERE FIELD_DEF_ID = 420),
Promo_Code as (SELECT RELATED_ID, VALUE_TX,
ROW_NUMBER() over (PARTITION BY RELATED_ID order by SYS_TM_STAMP desc) as ROW
FROM test.dbo.USER_FIELD_DATA
WHERE FIELD_DEF_ID = 484),
MM_Unit as (SELECT RELATED_ID, VALUE_TX,
ROW_NUMBER() over (PARTITION BY RELATED_ID order by SYS_TM_STAMP desc) as ROW
FROM test.dbo.USER_FIELD_DATA
WHERE FIELD_DEF_ID = 548),
Comm_Channel as (SELECT RELATED_ID, VALUE_TX,
ROW_NUMBER() over (PARTITION BY RELATED_ID order by SYS_TM_STAMP desc) as ROW
FROM test.dbo.USER_FIELD_DATA
WHERE FIELD_DEF_ID = 1064),
Comm_Broker as (SELECT RELATED_ID, VALUE_TX,
ROW_NUMBER() over (PARTITION BY RELATED_ID order by START_DT desc) as ROW
FROM test.dbo.USER_FIELD_DATA
WHERE FIELD_DEF_ID = 1065),
Comm_Agent as (SELECT RELATED_ID, VALUE_TX,
ROW_NUMBER() over (PARTITION BY RELATED_ID order by SYS_TM_STAMP desc) as ROW
FROM test.dbo.USER_FIELD_DATA
WHERE FIELD_DEF_ID = 1066),
Comm_Rate as (SELECT RELATED_ID, VALUE_TX,
ROW_NUMBER() over (PARTITION BY RELATED_ID order by SYS_TM_STAMP desc) as ROW
FROM test.dbo.USER_FIELD_DATA
WHERE FIELD_DEF_ID = 1067),
Comm_Unit as (SELECT RELATED_ID, VALUE_TX,
ROW_NUMBER() over (PARTITION BY RELATED_ID order by SYS_TM_STAMP desc) as ROW
FROM test.dbo.USER_FIELD_DATA
WHERE FIELD_DEF_ID = 1068),
CES_Contact as (SELECT RELATED_ID, VALUE_TX,
ROW_NUMBER() over (PARTITION BY RELATED_ID order by SYS_TM_STAMP desc) as ROW
FROM test.dbo.USER_FIELD_DATA
WHERE FIELD_DEF_ID = 1069),

REFERRAL_CODE as (SELECT RELATED_ID, VALUE_TX,
ROW_NUMBER() over (PARTITION BY RELATED_ID order by SYS_TM_STAMP desc) as ROW
FROM test.dbo.USER_FIELD_DATA
WHERE FIELD_DEF_ID = 1197),
RATE_PLAN as (
select pp.PRICE_PLAN_CD,
CASE
WHEN PP.START_DT > 20160000 THEN  SUBSTRING(pp.PRICE_PLAN_CD,7,1)
WHEN PP.START_DT < 20160000 THEN SUBSTRING(pp.PRICE_PLAN_CD,13,1)
END AS [RATE_PLAN]
FROM
PRICE_PLAN PP),
Implied_Margin as (SELECT RELATED_ID, VALUE_TX,
ROW_NUMBER() over (PARTITION BY RELATED_ID order by SYS_TM_STAMP desc) as ROW
FROM test.dbo.USER_FIELD_DATA
WHERE FIELD_DEF_ID = 1133)

SELECT
ldc_acct.LDC_ACCT_ID as CES_LDC_ID,
acct.ACCT_NO as CES_BILL_ACCT_NUM,
cust.CUST_ID as CES_CUST_NUM,
coalesce(ldc_acct.LDC_ACCT_NO, '') as UTIL_ACCT_NUM,
CASE
WHEN lctr.SYS_TM_STAMP > lctr.start_dt
THEN lctr.start_dt
ELSE cast(lctr.SYS_TM_STAMP as date)
END AS UTIL_ACCT_ACCT_CREATION_DT,
--coalesce(convert(char(10), convert(date, (convert(varchar(8), nullif(lctr.SYS_TM_STAMP, 0))), 113)),'') as  UTIL_ACCT_ACCT_CREATION_DT,
coalesce(convert(char(10), convert(date, (convert(varchar(8), nullif(ldc_acct.START_DT, 0))), 113)),'') as UTIL_ACCT_START_DT,
coalesce(convert(char(10), convert(date, (convert(varchar(8), nullif(ldc_acct.END_DT, 0))), 113)),'') as UTIL_ACCT_END_DT,
coalesce(meter.METER_NO, '') as UTIL_METER_NUM,
coalesce(ven.VENDOR_NM, '') as UTILITY,
coalesce(ldc_acct.CLASS_TY_CD, '') as SEGMENT,
coalesce(UPPER(acct.ACCT_NM), '') as CUST_COMPANY_NAME,
coalesce(UPPER(cust.FIRST_NM), '') as CUST_FIRSTNAME,
coalesce(UPPER(cust.COMPANY_LAST_NM), '') as CUST_LASTNAME,
coalesce(upper(addr.ADDR_1_TX), '') as SVC_ADDR_1,
coalesce(upper(addr.ADDR_2_TX), '') as SVC_ADDR_2,
coalesce(UPPER(addr.CITY_TX), '') as SVC_CITY,

--  *** Assign correct service/physical state -- Nexant has wrong states assigned for some locations
CASE
when ven.VENDOR_NM = 'Pacific Gas & Electric Co.' then 'CA'
when ven.VENDOR_NM = 'SoCal' then 'CA'
when ven.VENDOR_NM = 'San Diego Gas and Electric' then 'CA'
when ven.VENDOR_NM = 'Consumers Energy' then 'MI'
when ven.VENDOR_NM = 'DTE Energy' then 'MI'
when ven.VENDOR_NM = 'Michigan Gas Utilities' then 'MI'
when ven.VENDOR_NM = 'Semco Energy' then 'MI'
when ven.VENDOR_NM = 'Columbia Gas of testo' then 'test'
when ven.VENDOR_NM = 'Duke Energy Gas test' then 'test'
when ven.VENDOR_NM = 'Dominion (DEO)' then 'test'
when ven.VENDOR_NM = 'Black Hills - NE Ag' then 'NE'
when ven.VENDOR_NM = 'Black Hills - NE Central' then 'NE'
when ven.VENDOR_NM = 'Black Hills - NE West' then 'NE'
when ven.VENDOR_NM = 'Black Hills - WY Casper' then 'WY'
when ven.VENDOR_NM = 'Black Hills - WY Gillette' then 'WY'
when ven.VENDOR_NM = 'Black Hills - WY Torrington' then 'WY'
when ven.VENDOR_NM = 'Peoples Gas' then 'IL'
when ven.VENDOR_NM = 'Nicor Gas' then 'IL'
when ven.VENDOR_NM = 'North Shore Gas' then 'IL'
else ''
END AS SVC_STATE,

left(coalesce(addr.POSTAL_CD_TX, ''),5) as SVC_POSTAL_CODE,
coalesce(upper(mail.ADDR_1_TX), '') as MAIL_ADDR_1,
coalesce(upper(mail.ADDR_2_TX), '') as MAIL_ADDR_2,
coalesce(UPPER(mail.CITY_TX), '') as MAIL_CITY,
mail.STATE_TX as MAIL_STATE,
left(coalesce(mail.POSTAL_CD_TX, ''),5) as MAIL_POSTAL_CODE,
Cast(sum(distinct(musg.QTY_DELIVERED_NO))as Int) as USAGE_SUM,
Cast(count(distinct(musg.QTY_DELIVERED_NO)) as Int) as USAGE_CNT,
Cast((sum(distinct(musg.QTY_DELIVERED_NO))/count(distinct(musg.QTY_DELIVERED_NO))) as Int) as USAGE_MTH_EST,
Cast((sum(distinct(musg.QTY_DELIVERED_NO))/count(distinct(musg.QTY_DELIVERED_NO)))*12 as Int) as USAGE_YRLY_EST,
coalesce(pplan.PRICE_PLAN_CD, '') as CES_RATE_CODE,
coalesce(pplan.EXTERNAL_RATE_CD, '') as UTIL_RATE_CODE,
CASE
WHEN RP.RATE_PLAN = 'F' THEN 'Fixed'
WHEN RP.RATE_PLAN = 'M' THEN 'Managed'
WHEN RP.RATE_PLAN = 'N' THEN 'Index'
WHEN RP.RATE_PLAN = 'V' THEN ' Variable'
END AS RATE_PLAN,
coalesce(convert(char(10), convert(date, (convert(varchar(8), nullif(rate_grp.START_DT, 0))), 113)),'') as RATE_CODE_START_DATE,
coalesce(convert(char(10), convert(date, (convert(varchar(8), nullif(rate_grp.END_DT, 0))), 113)),'') as RATE_CODE_END_DATE,
CASE
WHEN RP.RATE_PLAN = 'V' THEN ''
WHEN substring(pplan.PRICE_PLAN_CD,0,2) ='NE' THEN DateDiff(Month, convert(date, (convert(varchar(8), nullif(rate_grp.START_DT, 0))), 113), convert(date, (convert(varchar(8), nullif(rate_grp.END_DT, 0))), 113) )
WHEN substring(pplan.PRICE_PLAN_CD,0,2) ='WY' THEN DateDiff(Month, convert(date, (convert(varchar(8), nullif(rate_grp.START_DT, 0))), 113), convert(date, (convert(varchar(8), nullif(rate_grp.END_DT, 0))), 113) )
ELSE substring(pplan.PRICE_PLAN_CD,11,2)
END as RATE_CODE_LENGTH,

coalesce(pindex.DESCRIPTION_TX, '') as RISK_CURVE_NEXANT,

-- Remap Risk Curves to correct for data issues in Nexant RM
case
-- Remap records with both null Risk Curves and null Rate Group End Dates to Month-to-Month Risk Curves
when pindex.DESCRIPTION_TX is null and rate_grp.END_DT = 0 then
case
when ven.VENDOR_NM = 'Pacific Gas & Electric Co.' then 'PG&E Choice Month-to-Month'
when ven.VENDOR_NM = 'SoCal' then 'SoCal Choice Month-to-Month'
when ven.VENDOR_NM = 'San Diego Gas and Electric' then 'SDG&E Choice Month-to-Month'
when ven.VENDOR_NM = 'Consumers Energy' then 'Consum Ch Month-to-Month'
when ven.VENDOR_NM = 'DTE Energy' then 'Michcon Choice Month-to-Month'
when ven.VENDOR_NM = 'Columbia Gas of testo' then 'Ctest Choice Month-to-Month'
when ven.VENDOR_NM = 'Duke Energy Gas test' then 'Duke Choice Month-to-Month'
when ven.VENDOR_NM = 'Dominion (DEO)' then 'DEO Choice Month-to-Month'
else coalesce(pindex.DESCRIPTION_TX, '')
end
-- Remap Managed Price and Fixed Term products with null Rate Group End Date or Expired Rate Group End Date to Month-to-Month Risk Curves.
when (right(pindex.DESCRIPTION_TX, 2) = 'MP' or pindex.DESCRIPTION_TX = 'Fixed Price')and (rate_grp.END_DT = 0 or convert(datetime, (convert(varchar(8), nullif(rate_grp.END_DT, 0))), 113) < GETDATE()) then
case
when ven.VENDOR_NM = 'Pacific Gas & Electric Co.' then 'PG&E Choice Month-to-Month'
when ven.VENDOR_NM = 'SoCal' then 'SoCal Choice Month-to-Month'
when ven.VENDOR_NM = 'San Diego Gas and Electric' then 'SDG&E Choice Month-to-Month'
when ven.VENDOR_NM = 'Consumers Energy' then 'Consum Ch Month-to-Month'
when ven.VENDOR_NM = 'DTE Energy' then 'Michcon Choice Month-to-Month'
when ven.VENDOR_NM = 'Columbia Gas of testo' then 'Ctest Choice Month-to-Month'
when ven.VENDOR_NM = 'Duke Energy Gas test' then 'Duke Choice Month-to-Month'
when ven.VENDOR_NM = 'Dominion (DEO)' then 'DEO Choice Month-to-Month'
else coalesce(pindex.DESCRIPTION_TX, '')
end
-- Remap California products to Fixed Price based on null Risk Curve, a non-zero price and an unexpired Rate Group End Date (can be eliminated when Nexant RM Indexes updated for CA).
when pindex.DESCRIPTION_TX is null and pplan_detail.PRICE_PER_UNIT_NO <> 0and ven.VENDOR_NM in ('Pacific Gas & Electric Co.', 'SoCal', 'San Diego Gas and Electric') then
case
when convert(datetime, (convert(varchar(8), nullif(rate_grp.END_DT, 0))), 113) >= GETDATE() then 'Fixed Price'
when dateadd(MONTH, datediff(MONTH, 0, convert(datetime, (convert(varchar(8), nullif(rate_grp.END_DT, 0))), 113)), 0) < GETDATE() then
-- Remap California products to Month-to-Month based on null Risk Curve, a non-zero price
case
when ven.VENDOR_NM = 'Pacific Gas & Electric Co.' then 'PG&E Choice Month-to-Month'
when ven.VENDOR_NM = 'SoCal' then'SoCal Choice Month-to-Month'
when ven.VENDOR_NM = 'San Diego Gas and Electric' then'SDG&E Choice Month-to-Month'
else coalesce(pindex.DESCRIPTION_TX, '')
end
else coalesce(pindex.DESCRIPTION_TX, '')
end
else coalesce(pindex.DESCRIPTION_TX, '')
END AS RISK_CURVE_REMAP,

-- Remap Risk Curves to match the logic for the Risk Curves in ELF (pushed current date to the next month to represent Prompt Month)
CASE
-- Remap records with both null Risk Curves and null Rate Group End Dates to Month-to-Month Risk Curves
when pindex.DESCRIPTION_TX is null and rate_grp.END_DT = 0 then
case
when ven.VENDOR_NM = 'Pacific Gas & Electric Co.' then 'PG&E Choice Month-to-Month'
when ven.VENDOR_NM = 'SoCal' then 'SoCal Choice Month-to-Month'
when ven.VENDOR_NM = 'San Diego Gas and Electric' then 'SDG&E Choice Month-to-Month'
when ven.VENDOR_NM = 'Consumers Energy' then 'Consum Ch Month-to-Month'
when ven.VENDOR_NM = 'DTE Energy' then 'Michcon Choice Month-to-Month'
when ven.VENDOR_NM = 'Columbia Gas of testo' then 'Ctest Choice Month-to-Month'
when ven.VENDOR_NM = 'Duke Energy Gas test' then 'Duke Choice Month-to-Month'
when ven.VENDOR_NM = 'Dominion (DEO)' then 'DEO Choice Month-to-Month'
else coalesce(pindex.DESCRIPTION_TX, '')
end
-- Remap Managed Price and Fixed Term products with null Rate Group End Date or Expired Rate Group End Date to Month-to-Month Risk Curves.
when (right(pindex.DESCRIPTION_TX, 2) = 'MP' or pindex.DESCRIPTION_TX = 'Fixed Price') and (rate_grp.END_DT = 0 or dateadd(MONTH, datediff(MONTH, 0, convert(datetime, (convert(varchar(8), nullif(rate_grp.END_DT, 0))), 113)), 0) < GETDATE()) then
case
when ven.VENDOR_NM = 'Pacific Gas & Electric Co.' then 'PG&E Choice Month-to-Month'
when ven.VENDOR_NM = 'SoCal' then 'SoCal Choice Month-to-Month'
when ven.VENDOR_NM = 'San Diego Gas and Electric' then 'SDG&E Choice Month-to-Month'
when ven.VENDOR_NM = 'Consumers Energy' then 'Consum Ch Month-to-Month'
when ven.VENDOR_NM = 'DTE Energy' then 'Michcon Choice Month-to-Month'
when ven.VENDOR_NM = 'Columbia Gas of testo' then 'Ctest Choice Month-to-Month'
when ven.VENDOR_NM = 'Duke Energy Gas test' then 'Duke Choice Month-to-Month'
when ven.VENDOR_NM = 'Dominion (DEO)' then 'DEO Choice Month-to-Month'
else coalesce(pindex.DESCRIPTION_TX, '')
end
-- Remap California products to Fixed Price based on null Risk Curve, a non-zero price and a future Rate Group End Date. (can be eliminated when Nexant RM Indexes updated for CA).
when pindex.DESCRIPTION_TX is null and pplan_detail.PRICE_PER_UNIT_NO <> 0 and ven.VENDOR_NM in ('Pacific Gas & Electric Co.', 'SoCal', 'San Diego Gas and Electric')  then
case
when convert(datetime, (convert(varchar(8), nullif(rate_grp.END_DT, 0))), 113) >= GETDATE() then 'Fixed Price'
-- Remap California products to Month-to-Month based on null Risk Curve, a non-zero price and an expired Rate Group End Date (can be eliminated when Nexant RM Indexes updated for CA).
when dateadd(MONTH, datediff(MONTH, 0, convert(datetime, (convert(varchar(8), nullif(rate_grp.END_DT, 0))), 113)), 0) < GETDATE() then
case
when ven.VENDOR_NM = 'Pacific Gas & Electric Co.' then 'PG&E Choice Month-to-Month'
when ven.VENDOR_NM = 'SoCal' then 'SoCal Choice Month-to-Month'
when ven.VENDOR_NM = 'San Diego Gas and Electric' then 'SDG&E Choice Month-to-Month'
else coalesce(pindex.DESCRIPTION_TX, '')
end
else coalesce(pindex.DESCRIPTION_TX, '')
end
else coalesce(pindex.DESCRIPTION_TX, '')
END AS RISK_CURVE_ELF,

coalesce(ldc_acct.STATUS_CD, '') as BILLING_STATUS,
ls.LIFECYCLE_STATUS,
-- Assign Report Status for each location
CASE
when ls.LIFECYCLE_STATUS = '01 Processing' then '01 Processing'
when ls.LIFECYCLE_STATUS in ('02 Utility Reject', '03 Ops Reject', '04 Cancelled') then '02 Reject/Cancel'
when ls.LIFECYCLE_STATUS in ('05 Pending Flow Start', '06 Active On Flow', '07 Pending Flow Stop') then '03 Active'
when ls.LIFECYCLE_STATUS in ('08 Inactive Off Flow', '09 Collections') then '04 Inactive'
when ls.LIFECYCLE_STATUS = '10 Status Error' then '05 Status Error'
END AS CUSTOMER_STATUS,
coalesce(pindexval.VALUE_NO, pplan_detail.PRICE_PER_UNIT_NO, 0) as PRICE,
coalesce(pplan_detail.BLOCK_UNIT_CD, '') as PRICE_UNITS,
coalesce(convert(char(10), convert(date, (convert(varchar(8), nullif(ldc_acct.START_DT, 0))), 113)),'') as SVC_START_DATE_CONF,
coalesce(convert(char(10), convert(date, (convert(varchar(8), nullif(ldc_acct.END_DT, 0))), 113)),'') as SVC_DROP_DATE_CONF,
coalesce(convert(date, (convert(varchar(8), nullif(esp.START_DT, 0))), 113),convert(date, (convert(varchar(8), nullif(acct.acct_creation_dt, 0))), 113)) as SALES_DATE,
lctr.start_dt AS CONTRACT_START_DT,
lctr.end_dt AS CONTRACT_END_DT,
CASE
when lctr.END_DT IS NULL THEN  ''
ELSE DATEDIFF(MONTH, lctr.START_DT, lctr.END_DT)
END as CONTRACT_LENGTH,

--coalesce(mc.VALUE_TX, '') as [Sales Channel for Enrollments],
--coalesce(mb.VALUE_TX, '') as [Vendor Used in Sale],
--coalesce(ma.VALUE_TX, '') as [Agent that completed sale],
coalesce(vid.VALUE_TX, '') as [TPV_ID],
--coalesce(fp.VALUE_TX, '') as [Fixed Percentage],
--coalesce(mcomm.VALUE_TX, '') as [Commission Amount],
coalesce(pc.VALUE_TX, '') as [Promo Code],
--coalesce(mu.VALUE_TX, '') as [Unit for Commission Payment],
coalesce(cc.VALUE_TX, '') as [CHANNEL],
coalesce(cb.VALUE_TX, '') as [PARTNER],
coalesce(ca.VALUE_TX, '') as [AGENT],	coalesce(cr.VALUE_TX, '') as [COMM RATE],
coalesce(cu.VALUE_TX, '') as [COMM PER UNIT],
coalesce(ces_c.VALUE_TX, '') as [CES CONTACT],
coalesce(IM.VALUE_TX, '') IMPLIED_MARGIN,

acctct.FIRST_NM AS ACCT_FIRST_NAME,
acctct.LAST_NM AS ACCT_LAST_NAME,
acctct.PHONE_NO AS ACCT_PHONE_NO,
acctct.EMAIL_ADDR_TX AS ACCT_EMAIL,

lct.FIRST_NM AS LDC_FIRST_NAME,
lct.LAST_NM AS LDC_LAST_NAME,
lct.PHONE_NO AS LDC_PHONE_NO,
lct.EMAIL_ADDR_TX AS LDC_EMIAL,
coalesce(RC.VALUE_TX, '') AS REFERRAL_CODE

FROM test.dbo.ACCOUNT acct
join test.dbo.LDC_ACCOUNT ldc_acct on acct.ACCT_ID = ldc_acct.ACCT_ID
join test.dbo.[ADDRESS] addr on ldc_acct.ADDR_ID = addr.ADDR_ID
join test.dbo.CUSTOMER cust on acct.CUST_ID = cust.CUST_ID
join #lifecycle_status ls on ls.ldc_acct_id = ldc_acct.LDC_ACCT_ID
left join test.dbo.VENDOR ven on ldc_acct.LDC_VENDOR_ID = ven.VENDOR_ID
-- sorts the Rating Group by the last time stamp and picks the most recent record
left join rate_grp on ldc_acct.LDC_ACCT_ID = rate_grp.LDC_ACCT_ID and rate_grp.ROW = 1
LEFT join RATE_PLAN RP on rate_grp.RATE_CD = RP.PRICE_PLAN_CD
left join METER meter
on ldc_acct.LDC_ACCT_ID = meter.RELATE_ID and meter.ROW = 1

left join test.dbo.PRICE_PLAN pplan on rate_grp.RATE_CD = pplan.PRICE_PLAN_CD
left join test.dbo.PRICE_PLAN_DETAIL pplan_detail
on pplan.PRICE_PLAN_ID = pplan_detail.RELATE_ID
and pplan_detail.RELATE_CLASS_NM = 'cPricePlan' and pplan_detail.CHARGE_TY_CD = 'USG'
left join test.dbo.PRICE_INDEX pindex on pplan_detail.PRICE_INDEX_ID = pindex.PRICE_INDEX_ID
left join pindexval on pindex.PRICE_INDEX_ID = pindexval.PRICE_INDEX_ID and pindexval.ROW = 1
-- end the selection of a single,  most recent rating group
left join test.dbo.MONTHLY_USAGE musg
on ldc_acct.LDC_ACCT_ID = musg.LDC_ACCT_ID
--and max(musg.SERVICE_PERIOD_END_DT)-musg.SERVICE_PERIOD_END_DT <=365
left join ESP_CONTRACT esp on esp.LDC_ACCT_ID = ldc_acct.LDC_ACCT_ID
left join MM_Channel mc on mc.RELATED_ID = ldc_acct.LDC_ACCT_ID and mc.ROW = 1
left join MM_Broker mb on mb.RELATED_ID = ldc_acct.LDC_ACCT_ID and mb.ROW = 1
left join MM_Agent ma on ma.RELATED_ID = ldc_acct.LDC_ACCT_ID and ma.ROW = 1
left join Verification_ID vid on vid.RELATED_ID = ldc_acct.LDC_ACCT_ID and vid.ROW = 1
left join Fixedpct fp on fp.RELATED_ID = ldc_acct.LDC_ACCT_ID and fp.ROW = 1
left join MM_Commission mcomm on mcomm.RELATED_ID = ldc_acct.LDC_ACCT_ID and mcomm.ROW = 1
left join Promo_Code pc on pc.RELATED_ID = ldc_acct.LDC_ACCT_ID and pc.ROW = 1
left join MM_Unit mu on mu.RELATED_ID = ldc_acct.LDC_ACCT_ID and mu.ROW = 1
left join Comm_Channel cc on cc.RELATED_ID = ldc_acct.LDC_ACCT_ID and cc.ROW = 1
left join Comm_Broker cb on cb.RELATED_ID = ldc_acct.LDC_ACCT_ID and cb.ROW = 1
left join Comm_Agent ca on ca.RELATED_ID = ldc_acct.LDC_ACCT_ID and ca.ROW = 1
left join Comm_Rate cr on cr.RELATED_ID = ldc_acct.LDC_ACCT_ID and cr.ROW = 1
left join Comm_Unit cu on cu.RELATED_ID = ldc_acct.LDC_ACCT_ID and cu.ROW = 1
left join CES_Contact ces_c on ces_c.RELATED_ID = ldc_acct.LDC_ACCT_ID and ces_c.ROW = 1
left join REFERRAL_CODE RC on RC.RELATED_ID = ldc_acct.LDC_ACCT_ID and RC.ROW = 1
left join INVOICE_DIST_INFO idi on idi.RELATE_ID = acct.ACCT_ID
left join [ADDRESS] mail on idi.ADDR_ID = mail.ADDR_ID
left join Implied_Margin IM on IM.RELATED_ID = ldc_acct.LDC_ACCT_ID and IM.ROW = 1
left join ##ldccontacts lct on lct.LDC_ACCT_ID = ldc_acct.LDC_ACCT_ID and (lct.CONTACT_TY_CD = 'PRIM' and lct.ROW = 1)
left join ##acctcontacts acctct on acctct.ACCT_ID = acct.ACCT_ID  and (acctct.CONTACT_TY_CD = 'PRIM' and acctct.ROW =1)
left join ##ldccontracts lctr on ldc_acct.LDC_ACCT_ID = lctr.LDC_ACCT_ID and lctr.ROW =1

-- filter out Corey's test record
WHERE
ldc_acct.LDC_ACCT_ID <> 15993
and not (ven.VENDOR_ID = 396 and len(ldc_acct.LDC_ACCT_NO) = 20
and coalesce(meter.METER_NO, '') <> '' and right(ldc_acct.LDC_ACCT_NO, 7) not like ('%' + meter.METER_NO)
and (select COUNT(*) from test..METER M2 where M2.RELATE_ID = ldc_acct.LDC_ACCT_ID and M2.END_DT = 0) > 1 )
--and (ls.LIFECYCLE_STATUS LIKE '06%' or ls.LIFECYCLE_STATUS LIKE '07%')
--and (ven.VENDOR_NM LIKE  '%Dominion%' or ven.VENDOR_NM LIKE '%DTE%' or ven.VENDOR_NM LIKE '%Consumers%')
-- other filters
-- and ls.LIFECYCLE_STATUS = 'Whatever'
-- and ldc_acct.LDC_ACCT_ID='206387'
-- and cc.VALUE_TX = 'Telemarket'
-- and cb.VALUE_TX = 'AGR TM'
-- and acct.acct_creation_dt > '20161101'

GROUP BY
ldc_acct.LDC_ACCT_ID,
acct.ACCT_NO,
ldc_acct.LDC_ACCT_NO,
cust.CUST_ID,
acct.ACCT_ID,
--meter.METER_NO,
acct.ACCT_NM,
ldc_acct.CLASS_TY_CD,
ldc_acct.STATUS_CD,
addr.ADDR_1_TX,
addr.ADDR_2_TX,
addr.CITY_TX,
--addr.STATE_TX,
addr.POSTAL_CD_TX,
cust.FIRST_NM,
cust.COMPANY_LAST_NM,
ven.VENDOR_NM,
pplan.PRICE_PLAN_CD,
pplan.EXTERNAL_RATE_CD,
rate_grp.START_DT,
rate_grp.END_DT,
pplan_detail.BLOCK_UNIT_CD,
pindexval.VALUE_NO,
pindex.DESCRIPTION_TX,
pplan_detail.PRICE_PER_UNIT_NO,
pplan_detail.PRICE_INDEX_ADD_CONST_NO,
pplan_detail.PRICE_INDEX_CAP_NO,
pplan_detail.PRICE_INDEX_FLOOR_NO,
ldc_acct.START_DT,
ldc_acct.END_DT,
esp.START_DT,
acct.acct_creation_dt,
mc.VALUE_TX,
mb.VALUE_TX,
ma.VALUE_TX,
vid.VALUE_TX,
fp.VALUE_TX,
mcomm.VALUE_TX,
pc.VALUE_TX,
mu.VALUE_TX,
cc.VALUE_TX,
cb.VALUE_TX,
ca.VALUE_TX,
cr.VALUE_TX,
cu.VALUE_TX,
ces_c.VALUE_TX,
mail.ADDR_1_TX,
mail.ADDR_2_TX,
mail.CITY_TX,
mail.STATE_TX,
mail.POSTAL_CD_TX,
ls.LIFECYCLE_STATUS,
RP.RATE_PLAN,
meter.METER_NO,
lct.FIRST_NM,
lct.LAST_NM,
lct.PHONE_NO,
lct.EMAIL_ADDR_TX,
IM.VALUE_TX,
lctr.SYS_TM_STAMP,
lctr.start_dt,
lctr.END_DT,
acctct.FIRST_NM,
acctct.LAST_NM,
acctct.PHONE_NO,
acctct.EMAIL_ADDR_TX,
RC.VALUE_TX"""
