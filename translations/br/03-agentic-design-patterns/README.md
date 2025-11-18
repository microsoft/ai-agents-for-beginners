<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d71524fe83a23829ae7a23b4031aaac8",
  "translation_date": "2025-11-13T12:14:18+00:00",
  "source_file": "03-agentic-design-patterns/README.md",
  "language_code": "br"
}
-->
[![Como Projetar Bons Agentes de IA](../../../translated_images/lesson-3-thumbnail.1092dd7a8f1074a5b26e35aa8f810814e05a22fed1765c20c14b2b508c7ae379.br.png)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_
# Princípios de Design de Agentes de IA

## Introdução

Existem muitas maneiras de pensar na construção de Sistemas de Agentes de IA. Dado que a ambiguidade é uma característica e não um problema no design de IA Generativa, às vezes é difícil para os engenheiros saberem por onde começar. Criamos um conjunto de Princípios de Design de UX centrados no ser humano para permitir que os desenvolvedores construam sistemas de agentes centrados no cliente para atender às suas necessidades de negócios. Esses princípios de design não são uma arquitetura prescritiva, mas sim um ponto de partida para equipes que estão definindo e desenvolvendo experiências de agentes.

De forma geral, os agentes devem:

- Ampliar e escalar as capacidades humanas (brainstorming, resolução de problemas, automação, etc.)
- Preencher lacunas de conhecimento (atualizar-me sobre domínios de conhecimento, tradução, etc.)
- Facilitar e apoiar a colaboração nas formas como preferimos trabalhar com outras pessoas
- Tornar-nos versões melhores de nós mesmos (por exemplo, coach de vida/gestor de tarefas, ajudando-nos a aprender habilidades de regulação emocional e mindfulness, construindo resiliência, etc.)

## Esta Lição Abrangerá

- O que são os Princípios de Design de Agentes
- Quais são algumas diretrizes a seguir ao implementar esses princípios de design
- Exemplos de uso dos princípios de design

## Objetivos de Aprendizagem

Após concluir esta lição, você será capaz de:

1. Explicar o que são os Princípios de Design de Agentes
2. Explicar as diretrizes para usar os Princípios de Design de Agentes
3. Entender como construir um agente usando os Princípios de Design de Agentes

## Os Princípios de Design de Agentes

![Princípios de Design de Agentes](../../../translated_images/agentic-design-principles.1cfdf8b6d3cc73c2b738951ee7b2043e224441d98babcf654be69d866120f93a.br.png)

### Agente (Espaço)

Este é o ambiente no qual o agente opera. Esses princípios informam como projetamos agentes para interagir em mundos físicos e digitais.

- **Conectar, não colapsar** – ajudar a conectar pessoas a outras pessoas, eventos e conhecimento acionável para possibilitar colaboração e conexão.
- Agentes ajudam a conectar eventos, conhecimento e pessoas.
- Agentes aproximam as pessoas. Eles não são projetados para substituir ou diminuir as pessoas.
- **Facilmente acessível, mas ocasionalmente invisível** – o agente opera principalmente em segundo plano e só nos alerta quando é relevante e apropriado.
  - O agente é facilmente descoberto e acessível para usuários autorizados em qualquer dispositivo ou plataforma.
  - O agente suporta entradas e saídas multimodais (som, voz, texto, etc.).
  - O agente pode transitar perfeitamente entre primeiro plano e segundo plano; entre proativo e reativo, dependendo da percepção das necessidades do usuário.
  - O agente pode operar de forma invisível, mas seu processo de fundo e colaboração com outros agentes são transparentes e controláveis pelo usuário.

### Agente (Tempo)

Este é o modo como o agente opera ao longo do tempo. Esses princípios informam como projetamos agentes interagindo entre passado, presente e futuro.

- **Passado**: Refletindo sobre a história que inclui estado e contexto.
  - O agente fornece resultados mais relevantes com base na análise de dados históricos mais ricos, além de apenas eventos, pessoas ou estados.
  - O agente cria conexões a partir de eventos passados e reflete ativamente sobre a memória para interagir com situações atuais.
- **Agora**: Incentivar mais do que notificar.
  - O agente incorpora uma abordagem abrangente para interagir com as pessoas. Quando um evento ocorre, o agente vai além de notificações estáticas ou outras formalidades estáticas. O agente pode simplificar fluxos ou gerar dinamicamente dicas para direcionar a atenção do usuário no momento certo.
  - O agente entrega informações com base no ambiente contextual, mudanças sociais e culturais e adaptadas à intenção do usuário.
  - A interação com o agente pode ser gradual, evoluindo/crescendo em complexidade para capacitar os usuários a longo prazo.
- **Futuro**: Adaptar e evoluir.
  - O agente se adapta a vários dispositivos, plataformas e modalidades.
  - O agente se adapta ao comportamento do usuário, necessidades de acessibilidade e é livremente personalizável.
  - O agente é moldado e evolui por meio de interação contínua com o usuário.

### Agente (Núcleo)

Estes são os elementos-chave no núcleo do design de um agente.

- **Aceitar a incerteza, mas estabelecer confiança**.
  - Um certo nível de incerteza do agente é esperado. A incerteza é um elemento-chave do design de agentes.
  - Confiança e transparência são camadas fundamentais do design de agentes.
  - Os humanos têm controle sobre quando o agente está ligado/desligado e o status do agente é claramente visível o tempo todo.

## As Diretrizes para Implementar Esses Princípios

Ao usar os princípios de design anteriores, siga as seguintes diretrizes:

1. **Transparência**: Informe ao usuário que a IA está envolvida, como ela funciona (incluindo ações passadas) e como fornecer feedback e modificar o sistema.
2. **Controle**: Permita que o usuário personalize, especifique preferências e personalize, e tenha controle sobre o sistema e seus atributos (incluindo a capacidade de esquecer).
3. **Consistência**: Busque experiências consistentes e multimodais em dispositivos e pontos de acesso. Use elementos de UI/UX familiares sempre que possível (por exemplo, ícone de microfone para interação por voz) e reduza ao máximo a carga cognitiva do cliente (por exemplo, busque respostas concisas, recursos visuais e conteúdo de 'Saiba Mais').

## Como Projetar um Agente de Viagem Usando Esses Princípios e Diretrizes

Imagine que você está projetando um Agente de Viagem, aqui está como você poderia pensar em usar os Princípios de Design e Diretrizes:

1. **Transparência** – Informe ao usuário que o Agente de Viagem é um agente habilitado por IA. Forneça algumas instruções básicas sobre como começar (por exemplo, uma mensagem de "Olá", exemplos de prompts). Documente isso claramente na página do produto. Mostre a lista de prompts que um usuário solicitou no passado. Deixe claro como fornecer feedback (botões de positivo e negativo, botão Enviar Feedback, etc.). Articule claramente se o agente tem restrições de uso ou tópicos.
2. **Controle** – Certifique-se de que está claro como o usuário pode modificar o agente após sua criação com coisas como o Prompt do Sistema. Permita que o usuário escolha o quão detalhado o agente deve ser, seu estilo de escrita e quaisquer restrições sobre o que o agente não deve falar. Permita que o usuário visualize e exclua quaisquer arquivos ou dados associados, prompts e conversas anteriores.
3. **Consistência** – Certifique-se de que os ícones para Compartilhar Prompt, adicionar um arquivo ou foto e marcar alguém ou algo sejam padrão e reconhecíveis. Use o ícone de clipe de papel para indicar upload/compartilhamento de arquivos com o agente e um ícone de imagem para indicar upload de gráficos.

## Exemplos de Código

- Python: [Framework de Agente](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Framework de Agente](./code_samples/03-dotnet-agent-framework.md)

## Tem Mais Perguntas sobre Padrões de Design de Agentes de IA?

Participe do [Discord do Azure AI Foundry](https://aka.ms/ai-agents/discord) para se conectar com outros aprendizes, participar de horários de atendimento e tirar suas dúvidas sobre Agentes de IA.

## Recursos Adicionais

- <a href="https://openai.com" target="_blank">Práticas para Governança de Sistemas de IA Agentes | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">Projeto HAX Toolkit - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Responsible AI Toolbox</a>

## Lição Anterior

[Explorando Frameworks de Agentes](../02-explore-agentic-frameworks/README.md)

## Próxima Lição

[Padrão de Design de Uso de Ferramentas](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->