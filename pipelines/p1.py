Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    PowerBIWrite_2 = Task(
        task_id = "PowerBIWrite_2", 
        component = "PowerBIWrite", 
        workspaceName = "", 
        datasetType = "datasetName", 
        datasetTables = [{"inputAlias" : "in0", "tableName" : "", "writeMode" : "overwrite", "overwriteSchema" : "No"}]
    )
    PowerBIWrite_1 = Task(
        task_id = "PowerBIWrite_1", 
        component = "PowerBIWrite", 
        workspaceName = "", 
        datasetType = "datasetName", 
        datasetTables = [{"inputAlias" : "in0", "tableName" : "", "writeMode" : "overwrite", "overwriteSchema" : "No"}]
    )
    p1__Aggregate_1 = Task(task_id = "p1__Aggregate_1", component = "Model", modelName = "p1__Aggregate_1")
    OrchestrationSource_1 = SourceTask(
        task_id = "OrchestrationSource_1", 
        component = "OrchestrationSource", 
        kind = "GCSSource", 
        connector = Connection(kind = "GCS"), 
        isNew = True, 
        format = CSVFormat(
          allowLazyQuotes = False, 
          allowEmptyColumnNames = True, 
          separator = ",", 
          nullValue = "", 
          encoding = "UTF-8", 
          header = True
        ), 
        fileOperationProperties = {"fileLoadingType" : "filepath", "includeFileNameColumn" : True}
    )
