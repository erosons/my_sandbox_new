SELECT DISTINCT trim(cast(a.account_id AS varchar)) AS external_id__c,
         (case
    WHEN ''='' THEN
    'Intelometry' end) AS external_source__c ,a.account_name AS OwnerID, cast(c.contract_amendment_start_date AS date) AS "Start Date" , cast(c.contract_amendment_end_date AS date ) AS "End Date" , CAST(c.contract_id AS varchar) ContractNumber , trim(cast(a.account_id AS varchar)) AS AccountId , timestampdiff(month,c.contract_amendment_start_date , c.contract_amendment_end_date) AS ContractTerm , c.contract_amendment_status AS Status , timestampdiff(month,current_date(), c.contract_amendment_end_date) AS OwnerExpirationNotice , c.contract_amendment_billing_product_template AS Product2Id , ' ' AS billingAddress, ' ' AS SpecialTerms , ' ' AS Description, ' ' AS CustomerSignedId , ' ' AS CustomerSignedTitle , ' ' AS CompanySignedDate, ' ' AS CustomerSignedDate
FROM "mp2-IntelometrySAAS"."intelometry_analysis_data".dbo.tbExtractContractAmendment c
JOIN "mp2-IntelometrySAAS"."intelometry_analysis_data".dbo.tbExtractContract cs
    ON c.contract_id =cs.contract_id
JOIN "mp2-IntelometrySAAS"."intelometry_analysis_data".dbo.tbExtractDataAccount a
    ON cs.account_id = a.account_id
JOIN "mp2-IntelometrySAAS"."intelometry_analysis_data".dbo.tbExtractBillingInvoice bi
    ON bi.account_id = cs.account_id
        AND bi.contract_id = c.contract_id
JOIN 
    (SELECT (case
        WHEN contract_rate >10 THEN
        contract_rate/1000 end) AS contract_rate,contract_amendment_id
    FROM 
        (SELECT DISTINCT contract_amendment_id,
         (case
            WHEN contract_amendment_variable_name='Price' THEN
            contract_amendment_variable_value
            WHEN contract_amendment_variable_name IN ('Evergreen - Adder Price ($/kWh','contract_price_kwh','fixed_price_kwh','Variable_rate_kwh','block_price_kwh') THEN
            contract_amendment_variable_value
            END ) AS contract_rate
        FROM 
            (SELECT contract_amendment_id,
         contract_amendment_variable_name,
         contract_amendment_variable_value
            FROM "mp2-IntelometrySAAS"."intelometry_analysis_data".dbo.tbExtractContractAmendmentVariable) AS price) AS final_price) AS price_select
                ON price_select.contract_amendment_id = c.contract_amendment_id
            JOIN "mp2-IntelometrySAAS"."intelometry_analysis_data".dbo.tbExtractBillingDistributionGroup dg
                ON dg.distribution_group_name= bi.invoice_invoice_group_name
            JOIN "mp2-IntelometrySAAS"."intelometry_analysis_data".dbo.tbExtractDataFacility f
                ON bi.invoice_invoice_group_name = f.facility_number
                    AND bi.account_id =f.account_id
            JOIN 
                (SELECT DISTINCT account_id,
        account_name AS operating_company
                FROM mp2IntelMsAccess.tbExtractDataOperatingCompany ) ca
                    ON ca.account_id =cs.operating_company_id --where c.contract_amendment_status ='Active'
                        AND a.account_type ='Customer'
                        AND ca.operating_company NOT IN ('Shell Energy Solutions','Steel City Energy','MP2 ENERGY TEXAS LLC 2 (LSE)','X_MP2 Energy IL, LLC','MP2 Energy LLC') ---and ae.account_name = 'Pioneer Natural Resources USA Inc.'
                        AND c.contract_amendment_end_date >= current_date()
                        AND c.contract_amendment_deal_type NOT LIKE '%Holdover%'
                GROUP BY  c.contract_amendment_pricing_product_type, bi.invoice_end_date, c.contract_amendment_end_date, a.account_name, c.contract_id, trim(cast(a.account_id AS varchar)), trim(cast(cs.contract_id AS varchar)), c.contract_amendment_start_date, c.contract_amendment_billing_product_template, c.contract_amendment_status, bi.invoice_invoice_group_name, dg.statement_group_distribution_group_id, facility_number, cast(f.facility_id AS varchar), price_select.contract_rate
                ORDER BY  trim(cast(a.account_id AS varchar)) DESC --statement_group_number=invoice_statement_group_number =contract_statement_group_numbe