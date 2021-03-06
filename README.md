
Analyzing Historical Inventory and Sales Data to Plan Demand and Optimize Item Stocking

Description:

Lean procurement is predicated on proactively maintaining an inventory that minimizes costs and maximizes revenue.  This means identifying items that aren't selling at acceptable quantities or margins, as well as targeting highly profitable items for potential increase in volume.  Modern data analysis techniques can make this process very efficient by quickly identifying items that meet pre-determined criteria at regular intervals.  With appropriate automation, this analysis can be achieved regularly and with little continuous effort.  In doing so, procurement teams may be armed with data that allows them to optimize their decision making. 

This project requires time series data showing how many units of a given item are sold over a period of time, cost and sell prices, lead times, and product categories. In order to ensure the appropriate data is available, gen_inv_data.py is designed to create a random data set meeting these needs.  

This project seeks to achieve the following, given a set of historical sales data:

> Calculate various sales metrics and KPIs related to them<br/>
	- Total units sold per year<br/>
	- Average units sold per month<br/>
	- Total cost, revenue and profit per item<br/>
	- Average cost, revenue, and profit per item sale<br/>
	- Group items into categories and determine the above for each category<br/>
	
> Identify items that are not meeting profitability standards, as well as items exceeding those standards<br/>
	- Compare units sold and profits to pre-determined targets<br/>
	- Populate a list of items that do not meet targets for potential elimination<br/>
	- Populate a list of items that notably exceed targets for potential increase<br/>
	- If there are other DCs which stock a given item, identify DCs which may meet targets<br/>
	
> Perform forecasting to anticipate demand<br/>
	- Determine seasonality per item and per item category<br/>
	- Perform appropriate analysis to determine confidence intervals for future sales periods<br/>
	- Compare true data to predicted data to verify accuracy<br/>
	- If accuracy is consistent and acceptable, suggest PAR levels that can adapt to changing demand<br/>
	- Populate a list of items that are below predicted demand <br/>
	
> Automate the tasks above<br/>
	- Configure Docker containers with Apache Airflow to orchestrate execution<br/>
	- Run updates that add new data over time and update a SQL Server table with the new data<br/>
	- Periodically ETL the data, loading to a human-readable format for procurement team to take action<br/>
	





