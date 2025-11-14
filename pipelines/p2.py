Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    tile = Task(
        task_id = "tile", 
        component = "Dataset", 
        table = {"name" : "tile", "sourceType" : "Table", "sourceName" : "ayush_demos.demos", "alias" : ""}
    )
    customer = Task(
        task_id = "customer", 
        component = "Dataset", 
        table = {"name" : "customer", "sourceType" : "Table", "sourceName" : "ayush_demos.demos", "alias" : ""}
    )
    p2__Aggregate_0 = Task(task_id = "p2__Aggregate_0", component = "Model", modelName = "p2__Aggregate_0")
    p2__XMLParse_1 = Task(task_id = "p2__XMLParse_1", component = "Model", modelName = "p2__XMLParse_1")
    Directory_1 = Task(task_id = "Directory_1", component = "Directory", integration = "", path = "")
    send_email = Task(
        task_id = "send_email", 
        component = "Email", 
        body = "", 
        subject = "", 
        includeData = False, 
        fileName = "", 
        to = ["ayush@gmail.com"], 
        connection = Connection(kind = "smtp", id = "smtp_1"), 
        fileFormat = "", 
        hasTemplate = False
    )
    new_sales = Task(
        task_id = "new_sales", 
        component = "Dataset", 
        table = {"name" : "new_sales", "sourceType" : "Table", "sourceName" : "ayush_demos.demos", "alias" : ""}
    )
