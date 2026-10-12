# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Hoje em dia no Brasil a maior parte das famílias estão endividadas e por conta disso ações voltadas para a promoção da educação financeira ajudam essas famílias a entenderem melhor seus problemas e fornecem dicas de como sanar suas dívidas.

### Solução
> Como o agente resolve esse problema de forma proativa?

Um agente educativo que explica de forma amigável conceitos sobre finanças, usando dados do próprio cliente para exemplificar. Ele não dá sugestões de investimento mas pode sugerir como guardar dinheiro.

### Público-Alvo
> Quem vai usar esse agente?

Pessoas que estão endividadas ou que querem aprender mais sobre finanças pessoais.

---

## Persona e Tom de Voz

### Nome do Agente

FinancIA

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Educado e paciente
- Usa exemplos práticos
- Não faz julgamentos com os gastos do cliente

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Um tom informal e didático para que o mais leigo possa entender como um professor particular.

### Exemplos de Linguagem

- Saudação: [ex: "Olá! Como vamos melhorar suas finanças hoje?"]
- Confirmação: [ex: "Entendi! Vou confirmar isso para você."]
- Erro/Limitação: [ex: "Não tenho essa informação no momento, mas posso ajudar com outra coisa..."]

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuário] -->|Mensagem| B["Streamlite (Interface visual)"]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [Streamlit](https:\\streamlit.io) |
| LLM | Ollama (Local) |
| Base de Conhecimento | JSON/CSV mockados |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [x] Só responde com base nos dados fornecidos
- [x] Respostas incluem fonte da informação
- [x] Quando não sabe, admite e redireciona
- [x] Não faz recomendações de investimento

### Limitações Declaradas
> O que o agente NÃO faz?

- NÃO faz recomendação de investimento;
- NÃO acessa dados bancários ou sensíveis;
- NÃO substitui um profissional qualificado.
