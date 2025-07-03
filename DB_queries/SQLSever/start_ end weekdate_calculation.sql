--- If the start date of the week is Sunday

Select dateadd(day,1-datepart(Weekday,getdate()),cast(getdate() as date)) => Startdate of the Week


--- If the End date of the week if the week starts from Sunday

Select dateadd(day,7-datepart(Weekday,getdate()),cast(getdate() as date)) => Startdate of the Week