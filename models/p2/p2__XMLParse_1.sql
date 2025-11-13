{{
  config({    
    "materialized": "ephemeral",
    "database": "ayush_demos",
    "schema": "demos"
  })
}}

WITH XMLParse_1 AS (

  {{ prophecy_basics.XMLParse('', '', 'parseFromSampleRecord', '', '') }}

)

SELECT *

FROM XMLParse_1
