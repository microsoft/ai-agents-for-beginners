# Agentes de IA para Iniciantes - Guia de Estudo & Resumo do Curso

Este guia fornece um resumo do curso "Agentes de IA para Iniciantes" e explica conceitos-chave, frameworks e padrões de design para construir Agentes de IA.

## 1. Introdução aos Agentes de IA

**O que são Agentes de IA?**
Agentes de IA são sistemas que estendem as capacidades dos Grandes Modelos de Linguagem (LLMs) ao dar-lhes acesso a **ferramentas**, **conhecimento** e **memória**. Ao contrário de um chatbot padrão de LLM que apenas gera texto com base nos dados de treino, um Agente de IA pode:
- **Perspetivar** o seu ambiente (através de sensores ou entradas).
- **Raciocinar** sobre como resolver um problema.
- **Agir** para mudar o ambiente (através de atuadores ou execução de ferramentas).

**Componentes Chave de um Agente:**
- **Ambiente**: O espaço onde o agente opera (ex. um sistema de reservas).
- **Sensores**: Mecanismos para recolher informação (ex. ler uma API).
- **Atuadores**: Mecanismos para realizar ações (ex. enviar um e-mail).
- **Cérebro (LLM)**: O motor de raciocínio que planeia e decide quais ações tomar.

## 2. Frameworks Agenticos

O curso cobre três frameworks principais para construir agentes:

| Framework | Foco | Melhor Para |
|-----------|-------|-------------|
| **Semantic Kernel** | SDK pronto para produção para .NET/Python | Aplicações empresariais, integração de IA com código existente. |
| **AutoGen** | Colaboração multiagente | Cenários complexos que exigem agentes especializados a comunicarem entre si. |
| **Azure AI Agent Service** | Serviço cloud gerido | Implementação segura e escalável com gestão de estado integrada. |

## 3. Padrões de Design Agenticos

Padrões de design ajudam a estruturar como os agentes operam para resolver problemas de forma fiável.

### **Padrão de Utilização de Ferramentas** (Lição 4)
Este padrão permite aos agentes interagir com o mundo exterior.
- **Conceito**: O agente recebe um "esquema" (uma lista de funções disponíveis e seus parâmetros). O LLM decide *qual* ferramenta usar e com *quais* argumentos com base no pedido do utilizador.
- **Fluxo**: Pedido do Utilizador -> LLM -> **Seleção da Ferramenta** -> **Execução da Ferramenta** -> LLM (com output da ferramenta) -> Resposta Final.
- **Casos de Uso**: Obtenção de dados em tempo real (tempo, preços de ações), realização de cálculos, execução de código.

### **Padrão de Planeamento** (Lição 7)
Este padrão permite aos agentes resolver tarefas complexas e multi-etapas.
- **Conceito**: O agente divide um objetivo de alto nível numa sequência de subtarefas menores.
- **Abordagens**:
  - **Decomposição da Tarefa**: Dividir "Planear uma viagem" em "Reservar voo", "Reservar hotel", "Alugar carro".
  - **Planeamento Iterativo**: Reavaliar o plano com base no resultado das etapas anteriores (ex. se o voo estiver lotado, escolher outra data).
- **Implementação**: Frequentemente envolve um agente "Planeador" que gera um plano estruturado (ex. JSON) que é depois executado por outros agentes.

## 4. Princípios de Design

Ao desenhar agentes, considere três dimensões:
- **Espaço**: Os agentes devem ligar pessoas e conhecimento, ser acessíveis mas discretos.
- **Tempo**: Os agentes devem aprender com o *Passado*, fornecer sugestões relevantes no *Presente* e adaptar-se para o *Futuro*.
- **Núcleo**: Abraçar a incerteza mas estabelecer confiança através da transparência e controlo do utilizador.

## 5. Resumo das Lições Principais

- **Lição 1**: Agentes são sistemas, não apenas modelos. Eles percebem, raciocinam e agem.
- **Lição 2**: Frameworks como Semantic Kernel e AutoGen abstraem a complexidade da chamada de ferramentas e gestão de estado.
- **Lição 3**: Projetar com transparência e controlo do utilizador em mente.
- **Lição 4**: Ferramentas são as "mãos" do agente. A definição do esquema é crucial para o LLM entender como usá-las.
- **Lição 7**: O planeamento é a "função executiva" do agente, permitindo-lhe enfrentar fluxos de trabalho complexos.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em consideração que traduções automatizadas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->