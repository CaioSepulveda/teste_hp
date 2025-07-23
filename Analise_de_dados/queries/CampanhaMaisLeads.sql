SELECT
    campanha,
    SUM(leads) AS total_leads
FROM
    teste_tecnico
GROUP BY
    campanha
ORDER BY
    total_leads DESC
LIMIT 1;