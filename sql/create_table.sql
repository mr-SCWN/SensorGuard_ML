DROP TABLE IF EXISTS machine_measurements ;

CREATE TABLE machine_measurements (
    udi                         INTEGER primary key,
    product_id                  TEXT,
    product_type                TEXT,
    air_temperature_k           REAL,
    process_temperature_k       REAL,
    rotational_speed_rpm        INTEGER,
    torque_nm                   REAL,
    tool_wear_min               INTEGER,
    machine_failure             INTEGER, -- machine failure , twf, ... - binary flag - 0=no, 1=yes -> integer
    twf                         INTEGER,
    hdf                         INTEGER,
    pwf                         INTEGER,
    osf                         INTEGER,
    rnf                         INTEGER
);