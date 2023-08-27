CREATE PROCEDURE UnpivotProducts()
BEGIN
    -- Increase the max length for GROUP_CONCAT
    SET SESSION group_concat_max_len = 1000000;
    
    -- Initialize the variable to hold case statements
    SET @case_stmt = NULL;
    
    -- Populate @case_stmt with SQL strings
    SELECT GROUP_CONCAT(
            'SELECT product_id, "', COLUMN_NAME, '" AS store, ', COLUMN_NAME, ' AS price FROM Products WHERE ', COLUMN_NAME,' IS NOT NULL' SEPARATOR " UNION "
        )
    INTO @case_stmt
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME="Products" AND COLUMN_NAME != "product_id";
    
    -- Assign the generated SQL to @sql_query
    SET @sql_query = @case_stmt;
    
    -- Prepare and execute the SQL query
    PREPARE final_sql_query FROM @sql_query;
    EXECUTE final_sql_query;
    
    -- Deallocate the prepared statement
    DEALLOCATE PREPARE final_sql_query;
END;
