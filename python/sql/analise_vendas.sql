SELECT categoria,
       SUM(valor) AS total_vendas
FROM vendas
GROUP BY categoria
ORDER BY total_vendas DESC;
