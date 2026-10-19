# Avaliação e Métricas

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

---

## Exemplos de Cenários de Teste

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** Valor baseado no `transacoes.csv`
- **Resultado:** [x] Correto  [ ] Incorreto
- **OBS:** Respondeu corretamente, trouxe os 120,00 + 450,00 = 570,00 referentes à alimentação

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil do cliente
- **Resultado:** [x] Correto  [ ] Incorreto
- **OBS:** Respondeu de acordo com o perfil do investidor, explicou um pouco sobre como funcionam os investimentos e explicou um pouco dos produtos que achou que faria sentido pro cliente, no caso Taxa SELIC e CDB.

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de finanças
- **Resultado:** [x] Correto  [ ] Incorreto
- **OBS:** Sugeriu acessar algum site sobre meteorologia, inclusive forneceu fontes confiáveis e perguntou se poderia ajudar com outra coisa relacionada às finanças.

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [x] Correto  [ ] Incorreto
- **OBS:** Não alucionou, respondeu que não conhecia o produto e recomendou os que ela tinha conhecimento.

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- O chat atendeu de forma bem satisfatória, usou bem os documentos fornecidos, respondeu dentro do escopo definido e não inventou nenhuma informação, com mais treinamento ficará ainda mais confiável.

**O que pode melhorar:**
- Acredito que treinar mais mesmo, fornecer mais documentação para ele ter mais base e histórico.
