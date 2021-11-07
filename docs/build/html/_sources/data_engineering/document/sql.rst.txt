

Big query Examples
======================

**Who are the top 100 “tip earners“**
--------------------------------------------------------------------------------------------------------------
 **Who are the top 100 “tip earners the taxi IDs that earn more money than others for the last 3months".**

.. code-block:: sql
   :linenos:

    SELECT taxi_id, sum(tips) as total_tips FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
    WHERE EXTRACT( DATE from trip_end_timestamp) between DATE_SUB(current_date(), INTERVAL 3 MONTH) and CURRENT_DATE()
    group by 1 order by 2 desc limit 100

**Count the number of sessions per taxi ID**
---------------------------------------------------------------------------------------------------------------------------------------------

**Count the number of sessions per taxi ID (We assume that a new session starts if at least 8 hours have passed since the previous trip)**

.. code-block:: sql
   :linenos:

    with trip_extract as (SELECT taxi_id,
    trip_start_timestamp,
    trip_end_timestamp,
    row_number() over(partition by taxi_id
    order by trip_start_timestamp,
    trip_end_timestamp) as trip_number,
    lag(trip_end_timestamp,1) over(partition by taxi_id
    order by trip_start_timestamp,
    trip_end_timestamp) as prev_trip_end_timestamp
    FROM  `bigquery-public-data.chicago_taxi_trips.taxi_trips`
    order by 1,4),

    session as (select taxi_id,
    case when trip_number =1 or timestamp_diff (trip_end_timestamp, trip_start_timestamp, hour) >=8 then 1
    else 0 end as sessions
    from trip_extract)
    select taxi_id, sum(sessions) as total_sessions from session group by 1 order by 2 desc