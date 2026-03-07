# Agentes de IA para Iniciantes - Guia de Estudo e Resumo do Curso

Este guia fornece um resumo do curso "Agentes de IA para Iniciantes" e explica conceitos chave, frameworks e padrões de design para construir Agentes de IA.

## 1. Introdução aos Agentes de IA

**O que são Agentes de IA?**
Agentes de IA são sistemas que estendem as capacidades dos Grandes Modelos de Linguagem (LLMs) ao lhes dar acesso a **ferramentas**, **conhecimento** e **memória**. Diferente de um chatbot padrão de LLM que apenas gera texto com base em dados de treinamento, um Agente de IA pode:
- **Perceber** seu ambiente (por meio de sensores ou entradas).
- **Raciocinar** sobre como resolver um problema.
- **Agir** para mudar o ambiente (por meio de atuadores ou execução de ferramentas).

**Componentes Chave de um Agente:**
- **Ambiente**: O espaço onde o agente opera (ex.: um sistema de reservas).
- **Sensores**: Mecanismos para coletar informações (ex.: leitura de uma API).
- **Atuadores**: Mecanismos para executar ações (ex.: envio de email).
- **Cérebro (LLM)**: O motor de raciocínio que planeja e decide quais ações executar.

## 2. Frameworks Agentes

O curso usa **Microsoft Agent Framework (MAF)** com o **Azure AI Foundry Agent Service V2** para construção de agentes:

| Componente | Foco | Ideal Para |
|------------|------|------------|
| **Microsoft Agent Framework** | SDK unificado Python/C# para agentes, ferramentas e fluxos de trabalho | Construção de agentes com ferramentas, fluxos de trabalho multiagentes e padrões de produção. |
| **Azure AI Foundry Agent Service** | Runtime em nuvem gerenciado | Implantação segura e escalável com gerenciamento de estado embutido, observabilidade e confiança. |

## 3. Padrões de Design para Agentes

Padrões de design ajudam a estruturar como agentes operam para resolver problemas de forma confiável.

### **Padrão de Uso de Ferramenta** (Lição 4)
Este padrão permite que agentes interajam com o mundo exterior.
- **Conceito**: O agente recebe um "esquema" (uma lista de funções disponíveis e seus parâmetros). O LLM decide *qual* ferramenta chamar e com *quais* argumentos baseado no pedido do usuário.
- **Fluxo**: Pedido do usuário -> LLM -> **Seleção da Ferramenta** -> **Execução da Ferramenta** -> LLM (com saída da ferramenta) -> Resposta Final.
- **Casos de Uso**: Obtenção de dados em tempo real (clima, preços de ações), realização de cálculos, execução de código.

### **Padrão de Planejamento** (Lição 7)
Este padrão permite que agentes resolvam tarefas complexas em múltiplas etapas.
- **Conceito**: O agente divide um objetivo de alto nível em uma sequência de subtarefas menores.
- **Abordagens**:
  - **Decomposição de Tarefa**: Dividir "Planejar uma viagem" em "Reservar voo", "Reservar hotel", "Alugar carro".
  - **Planejamento Iterativo**: Reavaliar o plano baseado na saída das etapas anteriores (ex.: se o voo estiver lotado, escolher uma data diferente).
- **Implementação**: Frequentemente envolve um agente "Planejador" que gera um plano estruturado (ex.: JSON) que é depois executado por outros agentes.

## 4. Princípios de Design

Ao projetar agentes, considere três dimensões:
- **Espaço**: Agentes devem conectar pessoas e conhecimento, ser acessíveis, porém discretos.
- **Tempo**: Agentes devem aprender com o *Passado*, fornecer estímulos relevantes no *Agora* e se adaptar para o *Futuro*.
- **Núcleo**: Abrace a incerteza, mas estabeleça confiança por meio de transparência e controle do usuário.

## 5. Resumo das Lições Principais

- **Lição 1**: Agentes são sistemas, não apenas modelos. Eles percebem, raciocinam e agem.
- **Lição 2**: Microsoft Agent Framework abstrai a complexidade da chamada de ferramentas e gerenciamento de estado.
- **Lição 3**: Projete com transparência e controle do usuário em mente.
- **Lição 4**: Ferramentas são as "mãos" do agente. A definição do esquema é crucial para o LLM entender como usá-las.
- **Lição 7**: Planejamento é a função "executiva" do agente, permitindo que ele lide com fluxos de trabalho complexos.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->