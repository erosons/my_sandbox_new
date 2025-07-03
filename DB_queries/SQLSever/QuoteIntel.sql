SELECT distinct
    min(cast(q.quote_create_dttm as date)) as quote_created_date_min,
    min(cast(q.quote_create_dttm as date)) as quote_created_date_max,
    max(cast(q.quote_expiration_dttm as date)) as quote_expiration_date,
    q.quote_number,
    max(q.quote_version) as number_quotes,
    q.quote_operating_company as operating_company,
    q.quote_opportunity_type as opportunity_type,
    sub_c.customerName,
    --q.quote_account as customer_name,
    'Intelometry' as Platform,
    'ERCOT' as ISO,
    'TX' as State,
    cast(min(q.quote_start_date) as date) as quote_start_date,
    max(sub_base.quote_executed) as contract_executed_date,
    q.quote_sales_person as salesperson,
    q.quote_broker as broker,
    max(sub_base.grossmarginrate) as contracted_gross_margin_rate,
    max(sub_base.brokerfee) as contracted_broker_fee,
    max(sub_base.contractedvolume) as contracted_total_volume,
    max(sub_base.term) as contracted_term,
    max(sub_base.adder) as contracted_adder,
    max(sub_base.contractrate) as contracted_rate,
    max(sub_q.quote_term_broker_fee) as quote_broker_fee,
    max(sub_q.quote_term_margin_fee) as quote_margin_fee,
    Max(sub_q.quote_term) as quote_term,
    max(sub_q.quote_term_usage) as quote_total_volume,
    sub_base.contract_amendment_deal_type,
    sub_base.product,
    --sub_m.quote_meter_utility as ldc,
    sub_c.LDC,
    sub_m.num_accounts as num_ldcaccounts
FROM
    "mp2-IntelometrySAAS"."intelometry_analysis_data".dbo.tbExtractQuote q
    left join (
        SELECT 
            quote_id, 
            count(*) as num_accounts 
        FROM
            "mp2-IntelometrySAAS"."intelometry_analysis_data".dbo.tbExtractQuotemeter q 
        GROUP BY 
            quote_id
    ) sub_m on sub_m.quote_id = q.quote_id
    Left join (
        SELECT distinct
            cast(q.quote_create_dttm as date) as created_date,
            --q.quote_account,
            q.quote_number,
            q.quote_version,
            q.quote_opportunity_type,
            cast(sub_c.quote_executed_dttm as date) as quote_executed,
            cast(q.quote_start_date as date) as quote_start,
            sub_c.contract_account_name,
            sub_c.contract_amendment_deal_type,
            q.quote_sales_person,
            q.quote_broker,
            sub_c.brokerfee,
            sub_c.contractedvolume,
            sub_c.grossmarginrate,
            sub_c.term,
            sub_c.product,
            sub_c.adder,
            sub_c.contractrate
        FROM
            "mp2-IntelometrySAAS"."intelometry_analysis_data".dbo.tbExtractQuote q
            left join (
                SELECT
                    c.contract_account_name,
                    ca.contract_amendment_deal_type,
                    ca.contract_amendment_quote_number,
                    CAST(sub_qmax.quote_executed_dttm AS DATE) AS quote_executed_dttm,
                    sub_qmax.max_version,
                    CAST(o.brokerfee AS FLOAT) AS brokerfee,
                    CAST(o.contractedvolume AS FLOAT) AS contractedvolume, 
                    CAST(o.grossmarginrate AS FLOAT) AS grossmarginrate,
                    o.term,
                    o.product,
                    CAST(o.adder AS FLOAT) AS adder,
                    CAST(o.contractrate AS FLOAT) AS contractrate
                FROM
                    "mp2-IntelometrySAAS"."intelometry_analysis_data".dbo.tbExtractContract c
                    LEFT JOIN "mp2-IntelometrySAAS"."intelometry_analysis_data".dbo.tbExtractContractAmendment ca on c.contract_id = ca.contract_id
                    LEFT JOIN (
                        SELECT 
                            CAST(qx.quote_number AS VARCHAR) AS quote_number, 
                            CAST(qx.quote_executed_dttm AS DATE) AS quote_executed_dttm, 
                            max(qx.quote_version) as max_version 
                        FROM
                            "mp2-IntelometrySAAS"."intelometry_analysis_data".dbo.tbExtractQuote qx 
                        WHERE 
                            qx.quote_create_dttm >= '2020-01-01' 
                        GROUP BY 
                            qx.quote_number, 
                            qx.quote_executed_dttm
                    ) sub_qmax on sub_qmax.quote_number = ca.contract_amendment_quote_number 
                    left join (
                        SELECT DISTINCT
                            brokerfee,
                            customerName,
                            contractedvolume, 
                            grossmarginrate,
                            LDC,
                            LDC_ACCOUNT_NUMBER,
                            term,
                            product,
                            adder,
                            contractrate,
                            quoteNumber
                        FROM
                            "mp2-odin-raw"."deals_facilities" d
                        WHERE 
                            d.iso = 'ERCOT' 
                            and d.quotenumber is not null
                            and d.customerName not like '@%'
                    ) o on ca.contract_amendment_quote_number = o.quoteNumber 
            ) sub_c on sub_c.contract_amendment_quote_number = q.quote_number and sub_c.max_version = q.quote_version
        WHERE
            q.quote_broker not like '@%'
            and q.quote_create_dttm >= '2020-01-01'
            and q.quote_executed_dttm is not null
            and q.quote_title not like '%add%'
    ) as sub_base on sub_base.quote_number = q.quote_number and sub_base.quote_version = q.quote_version
    left join (
        SELECT DISTINCT
            qt2.quote_id,
            qt2.quote_version_number,
            qt2.quote_term,
            (qt2.quote_term_usage/1000) as quote_term_usage,
            sub_t."Broker Fee" as quote_term_broker_fee,
            sub_t.Margin as quote_term_margin_fee
        FROM
            "mp2-IntelometrySAAS"."intelometry_analysis_data".dbo.tbExtractQuoteTerm qt2
            left join (
                SELECT DISTINCT
                    quote_id, 
                    quote_Version_id, 
                    quote_term, 
                    CASE WHEN quote_term_charge_category = 'Broker Fee' THEN MAX(quote_term_price) ELSE NULL END AS "Broker Fee",
                    CASE WHEN quote_term_charge_category = 'Margin' THEN MAX(quote_term_price) ELSE NULL END AS "Margin"
                from (
                    select * 
                    from 
                        "mp2-IntelometrySAAS"."intelometry_analysis_data".dbo.tbExtractQuoteTermCharge c 
                    where 
                        c.quote_term_charge_category in ('Broker Fee','Margin')
		        ) as sourcetable
                GROUP BY
                    quote_id, 
                    quote_Version_id, 
                    quote_term, 
                    quote_term_charge_category
            ) as sub_t on qt2.quote_id = sub_t.quote_id and qt2.quote_version_id = sub_t.quote_version_id
		left join (
            SELECT 
                qt.quote_id, 
                --qt.quote_version_number, 
                max(qt.quote_term) as max_term
            FROM 
                "mp2-IntelometrySAAS"."intelometry_analysis_data".dbo.tbExtractQuoteTerm qt
            GROUP BY 
                qt.quote_id, 
                qt.quote_version_number
		) sub_q2 on sub_q2.quote_id = qt2.quote_id and sub_q2.max_term = qt2.quote_term 
    ) sub_q on sub_q.quote_number = q.quote_number 
WHERE
    q.quote_account not like '@%'
    and q.quote_create_dttm >= '2020-01-01'
    and q.quote_broker not like '@%'
    and q.quote_title not like'%add%'
    and q.quote_operating_company not in ('Steel City Energy','MP2 ENERGY TEXAS LLC 2 (LSE)','MP2 Energy NE, LLC','X_MP2 Energy IL, LLC')
GROUP BY
    q.quote_number,
    q.quote_operating_company,
    q.quote_opportunity_type,
    sub_c.customerName,
    --q.quote_account,
    q.quote_sales_person,
    q.quote_broker,
    sub_base.contract_amendment_deal_type,
    sub_base.product,
   -- sub_m.quote_meter_utility,
    sub_m.num_accounts

            
