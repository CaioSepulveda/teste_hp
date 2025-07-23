SELECT
    campanha,
    SUM(investimento) AS total_investimento,
    SUM(leads) AS total_leads,
    (SUM(investimento) / SUM(leads)) AS cpl
FROM
    teste_tecnico
GROUP BY
    campanha
-- Adicionar uma condição para evitar divisão por zero se houver campanhas sem leads
HAVING
    SUM(leads) > 0
ORDER BY
    cpl ASC
LIMIT 1;