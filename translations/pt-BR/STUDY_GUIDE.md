# Agentes de IA para Iniciantes - Guia de Estudo & Resumo do Curso

Este guia fornece um resumo do curso "Agentes de IA para Iniciantes" e explica conceitos chave, frameworks e padrões de design para construir Agentes de IA.

## 1. Introdução aos Agentes de IA

**O que são Agentes de IA?**  
Agentes de IA são sistemas que estendem as capacidades dos Modelos de Linguagem Grande (LLMs) dando-lhes acesso a **ferramentas**, **conhecimento** e **memória**. Diferente de um chatbot padrão de LLM que apenas gera texto com base nos dados de treinamento, um Agente de IA pode:  
- **Perceber** seu ambiente (via sensores ou entradas).  
- **Raciocinar** sobre como resolver um problema.  
- **Agir** para mudar o ambiente (via atuadores ou execução de ferramentas).  

**Componentes Chave de um Agente:**  
- **Ambiente**: O espaço onde o agente opera (ex.: um sistema de reservas).  
- **Sensores**: Mecanismos para reunir informações (ex.: leitura de uma API).  
- **Atuadores**: Mecanismos para realizar ações (ex.: enviar um e-mail).  
- **Cérebro (LLM)**: O motor de raciocínio que planeja e decide quais ações tomar.  

## 2. Frameworks Agentes

O curso utiliza o **Microsoft Agent Framework (MAF)** com o **Azure AI Foundry Agent Service V2** para construir agentes:

| Componente | Foco | Melhor Para |
|------------|-------|-------------|
| **Microsoft Agent Framework** | SDK unificado Python/C# para agentes, ferramentas e fluxos de trabalho | Construção de agentes com ferramentas, fluxos multiagentes e padrões de produção. |
| **Azure AI Foundry Agent Service** | Runtime gerenciado na nuvem | Implantação segura, escalável com gestão de estado, observabilidade e confiança integradas. |

## 3. Padrões de Design Agentes

Padrões de design ajudam a estruturar como agentes operam para resolver problemas de forma confiável.

### **Padrão de Uso de Ferramenta** (Lição 4)  
Este padrão permite que agentes interajam com o mundo externo.  
- **Conceito**: O agente recebe um "schema" (uma lista de funções disponíveis e seus parâmetros). O LLM decide *qual* ferramenta chamar e com *quais* argumentos baseado na solicitação do usuário.  
- **Fluxo**: Solicitação do Usuário -> LLM -> **Seleção da Ferramenta** -> **Execução da Ferramenta** -> LLM (com saída da ferramenta) -> Resposta Final.  
- **Casos de Uso**: Recuperar dados em tempo real (clima, preços de ações), realizar cálculos, executar código.  

### **Padrão de Planejamento** (Lição 7)  
Este padrão permite que agentes resolvam tarefas complexas e de múltiplas etapas.  
- **Conceito**: O agente divide uma meta de alto nível em uma sequência de subtarefas menores.  
- **Abordagens**:  
  - **Decomposição de Tarefa**: Dividir "Planejar uma viagem" em "Reservar voo", "Reservar hotel", "Alugar carro".  
  - **Planejamento Iterativo**: Reavaliar o plano com base na saída dos passos anteriores (ex.: se o voo estiver lotado, escolher outra data).  
- **Implementação**: Frequentemente envolve um agente "Planejador" que gera um plano estruturado (ex.: JSON) que é então executado por outros agentes.  

## 4. Princípios de Design

Ao projetar agentes, considere três dimensões:  
- **Espaço**: Agentes devem conectar pessoas e conhecimento, ser acessíveis mas discretos.  
- **Tempo**: Agentes devem aprender com o *Passado*, fornecer incentivos relevantes no *Presente* e se adaptar para o *Futuro*.  
- **Núcleo**: Aceitar incertezas mas estabelecer confiança através de transparência e controle do usuário.  

## 5. Resumo das Lições Principais

- **Lição 1**: Agentes são sistemas, não apenas modelos. Eles percebem, raciocinam e agem.  
- **Lição 2**: O Microsoft Agent Framework abstrai a complexidade da chamada de ferramentas e gestão de estado.  
- **Lição 3**: Projetar com transparência e controle do usuário em mente.  
- **Lição 4**: Ferramentas são as "mãos" do agente. Definição do schema é crucial para o LLM entender como usá-las.  
- **Lição 7**: Planejamento é a "função executiva" do agente, permitindo enfrentar fluxos de trabalho complexos.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em sua língua nativa deve ser considerado a fonte oficial. Para informações críticas, recomenda-se tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->