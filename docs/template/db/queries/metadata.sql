-- name: get_version_database
SELECT 
    version, 
    date 
    FROM VERSION_DATABASE 
    WHERE active = TRUE