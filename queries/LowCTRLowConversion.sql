WITH CampanhaMetricas AS (
    -- CTE 1: Calcula CTR e Taxa de Conversão para CADA campanha
    SELECT
        Campanha,
        -- Calcular CTR (Cliques / Impressões)
        (SUM(Cliques)::NUMERIC / NULLIF(SUM(impressoes), 0)) * 100 AS CTR,
        -- Calcular Taxa de Conversão (Leads / Cliques)
        (SUM(Leads)::NUMERIC / NULLIF(SUM(Cliques), 0)) * 100 AS Tx_Conv_Leads
    FROM
        teste_tecnico
    GROUP BY
        Campanha
    -- Excluir campanhas que não geraram impressões ou cliques para os cálculos
    HAVING SUM(impressoes) > 0 AND SUM(Cliques) > 0
),
MedianasGerais AS (
    -- CTE 2: Calcula a mediana do CTR e da Taxa de Conversão de TODAS as campanhas
    SELECT
        -- Mediana do CTR
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY CTR) AS Mediana_CTR,
        -- Mediana da Taxa de Conversão
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY Tx_Conv_Leads) AS Mediana_Tx_Conv_Leads
    FROM
        CampanhaMetricas
)
-- Consulta Final: Seleciona campanhas que atendem aos novos critérios
SELECT
    cm.Campanha,
    cm.CTR,
    mg.Mediana_CTR,
    cm.Tx_Conv_Leads,
    mg.Mediana_Tx_Conv_Leads
FROM
    CampanhaMetricas cm, -- Pegamos as métricas de cada campanha
    MedianasGerais mg    -- Pegamos os valores das medianas globais
WHERE
    cm.CTR < mg.Mediana_CTR            -- CTR abaixo da mediana
    AND cm.Tx_Conv_Leads < mg.Mediana_Tx_Conv_Leads -- E Taxa de Conversão abaixo da mediana
ORDER BY
    cm.CTR ASC,          -- Ordena por CTR crescente (os "piores" CTRs primeiro)
    cm.Tx_Conv_Leads ASC; -- E por Tx. Conv. crescente (as "piores" taxas de conversão primeiro)