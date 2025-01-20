use AdventureWorks2019

Select 
Name as StateName,
[CA] as Canada,
[US] as USA
FROM
(
    Select ad.AddressLine1,sp.Name,sp.CountryRegionCode 
    from person.Address ad
    join person.StateProvince sp
    on ad.StateProvinceID = sp.StateProvinceID ) comtab
PIVOT
    (
    Count(AddressLine1) FOR CountryRegionCode IN ([US],[CA])
    ) AS Pvt