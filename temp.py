def generate_query():
    query = """
    \copy (SELECT
    content
    FROM
        message
    WHERE
        channel_id IN (
            SELECT
                *
            FROM
                channels)
        AND NOT content IS NULL
        AND date > '2021-%s-01'
        AND date < '2021-%s-01')
        TO '~/pua-channels-21%s01-21%s01.csv' WITH CSV DELIMITER ',';
    """
    for i in range(1, 12):
        one = str(i).zfill(2)
        two = str(i + 1).zfill(2)
        print(query % (one, two, one, two))
