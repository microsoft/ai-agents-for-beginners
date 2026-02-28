# Agentes de IA para Iniciantes - Guia de Estudo e Resumo do Curso

Este guia fornece um resumo do curso "Agentes de IA para Iniciantes" e explica conceitos-chave, frameworks e padrões de design para construir Agentes de IA.

## 1. Introdução aos Agentes de IA

**O que são Agentes de IA?**
Os Agentes de IA são sistemas que estendem as capacidades dos Large Language Models (LLMs) dando-lhes acesso a **ferramentas**, **conhecimento** e **memória**. Ao contrário de um chatbot LLM padrão que apenas gera texto com base nos dados de treino, um Agente de IA pode:
- **Perceber** o seu ambiente (via sensores ou entradas).
- **Raciocinar** sobre como resolver um problema.
- **Agir** para alterar o ambiente (via atuadores ou execução de ferramentas).

**Componentes-chave de um Agente:**
- **Ambiente**: O espaço onde o agente opera (por exemplo, um sistema de reservas).
- **Sensores**: Mecanismos para recolher informação (por exemplo, leitura de uma API).
- **Atuadores**: Mecanismos para executar ações (por exemplo, envio de um email).
- **Cérebro (LLM)**: O motor de raciocínio que planeia e decide que ações tomar.

## 2. Frameworks Agenticos

O curso utiliza **Microsoft Agent Framework (MAF)** com **Azure AI Foundry Agent Service V2** para construir agentes:

| Component | Focus | Best For |
|-----------|-------|----------|
| **Microsoft Agent Framework** | Unified Python/C# SDK for agents, tools, and workflows | Building agents with tools, multi-agent workflows, and production patterns. |
| **Azure AI Foundry Agent Service** | Managed cloud runtime | Secure, scalable deployment with built-in state management, observability, and trust. |

## 3. Padrões de Design para Agentes

Os padrões de design ajudam a estruturar como os agentes operam para resolver problemas de forma fiável.

### **Padrão de Utilização de Ferramentas** (Lição 4)
Este padrão permite que os agentes interajam com o mundo exterior.
- **Conceito**: O agente recebe um "esquema" (uma lista de funções disponíveis e os seus parâmetros). O LLM decide *qual* ferramenta chamar e com *quais* argumentos com base no pedido do utilizador.
- **Fluxo**: Pedido do Utilizador -> LLM -> **Seleção da Ferramenta** -> **Execução da Ferramenta** -> LLM (com a saída da ferramenta) -> Resposta Final.
- **Casos de Uso**: Obter dados em tempo real (tempo, preços de ações), efetuar cálculos, executar código.

### **Padrão de Planeamento** (Lição 7)
Este padrão permite que os agentes resolvam tarefas complexas e com vários passos.
- **Conceito**: O agente divide um objetivo de alto nível numa sequência de subtarefas mais pequenas.
- **Abordagens**:
  - **Decomposição de Tarefas**: Dividir "Planear uma viagem" em "Reservar voo", "Reservar hotel", "Alugar carro".
  - **Planeamento Iterativo**: Reavaliar o plano com base na saída de passos anteriores (por exemplo, se o voo estiver cheio, escolher outra data).
- **Implementação**: Frequentemente envolve um agente "Planeador" que gera um plano estruturado (por exemplo, JSON) que é então executado por outros agentes.

## 4. Princípios de Design

Ao desenhar agentes, considere três dimensões:
- **Espaço**: Os agentes devem ligar pessoas e conhecimento, ser acessíveis mas discretos.
- **Tempo**: Os agentes devem aprender com o *Passado*, fornecer sugestões relevantes no *Agora*, e adaptar-se para o *Futuro*.
- **Núcleo**: Aceitar a incerteza, mas estabelecer confiança através da transparência e do controlo do utilizador.

## 5. Resumo das Lições Principais

- **Lição 1**: Os agentes são sistemas, não apenas modelos. Eles percebem, raciocinam e atuam.
- **Lição 2**: O Microsoft Agent Framework abstrai a complexidade da chamada de ferramentas e da gestão de estado.
- **Lição 3**: Conceber com transparência e controlo do utilizador em mente.
- **Lição 4**: As ferramentas são as "mãos" do agente. A definição do esquema é crucial para o LLM compreender como usá-las.
- **Lição 7**: O planeamento é a "função executiva" do agente, permitindo-lhe enfrentar fluxos de trabalho complexos.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Isenção de responsabilidade**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos empenhemos em garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original, no seu idioma nativo, deve ser considerado a fonte autoritativa. Para informação crítica, recomenda-se uma tradução profissional realizada por um tradutor humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->