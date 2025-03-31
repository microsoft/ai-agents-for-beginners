<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "969885aab5f923f67f134ce115fbbcaf",
  "translation_date": "2025-03-28T11:48:12+00:00",
  "source_file": "03-agentic-design-patterns\\README.md",
  "language_code": "pt"
}
-->
[![Como projetar bons agentes de IA](../../../translated_images/lesson-3-thumbnail.fc00fd0f7e476e3f6dbe06f4c10d1590953810d345283f825e79bede5e97e6d6.pt.png)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_
# Princípios de Design de Agentes de IA

## Introdução

Existem várias maneiras de pensar na construção de Sistemas de Agentes de IA. Dado que a ambiguidade é uma característica e não um problema no design de IA generativa, às vezes é difícil para os engenheiros saberem por onde começar. Criamos um conjunto de Princípios de Design de UX centrados no humano para permitir que os desenvolvedores construam sistemas de agentes centrados no cliente e atendam às suas necessidades de negócios. Esses princípios de design não são uma arquitetura prescritiva, mas sim um ponto de partida para equipes que estão definindo e desenvolvendo experiências com agentes.

Em geral, os agentes devem:

- Ampliar e escalar as capacidades humanas (brainstorming, resolução de problemas, automação, etc.)
- Preencher lacunas de conhecimento (me atualizar sobre domínios de conhecimento, tradução, etc.)
- Facilitar e apoiar a colaboração nas formas que preferimos trabalhar com os outros
- Tornar-nos versões melhores de nós mesmos (por exemplo, coach de vida/gestor de tarefas, ajudando-nos a aprender habilidades de regulação emocional e mindfulness, construir resiliência, etc.)

## Esta lição abordará

- O que são os Princípios de Design de Agentes
- Quais são algumas diretrizes para seguir ao implementar esses princípios de design
- Exemplos de uso dos princípios de design

## Objetivos de aprendizado

Após completar esta lição, você será capaz de:

1. Explicar o que são os Princípios de Design de Agentes
2. Explicar as diretrizes para usar os Princípios de Design de Agentes
3. Entender como construir um agente usando os Princípios de Design de Agentes

## Os Princípios de Design de Agentes

![Princípios de Design de Agentes](../../../translated_images/agentic-design-principles.9f32a64bb6e2aa5a1bdffb70111aa724058bc248b1a3dd3c6661344015604cff.pt.png)

### Agente (Espaço)

Este é o ambiente no qual o agente opera. Esses princípios informam como projetamos agentes para atuar em mundos físicos e digitais.

- **Conectar, não colapsar** – ajudar a conectar pessoas a outras pessoas, eventos e conhecimentos acionáveis para possibilitar colaboração e conexão.
  - Os agentes ajudam a conectar eventos, conhecimento e pessoas.
  - Os agentes aproximam as pessoas. Eles não são projetados para substituir ou diminuir as pessoas.
- **Facilmente acessível, mas ocasionalmente invisível** – o agente opera em grande parte em segundo plano e só nos alerta quando é relevante e apropriado.
  - O agente é facilmente descoberto e acessível para usuários autorizados em qualquer dispositivo ou plataforma.
  - O agente suporta entradas e saídas multimodais (som, voz, texto, etc.).
  - O agente pode alternar perfeitamente entre primeiro plano e segundo plano; entre proativo e reativo, dependendo da percepção das necessidades do usuário.
  - O agente pode operar de forma invisível, mas seu caminho de processo em segundo plano e colaboração com outros agentes são transparentes e controláveis pelo usuário.

### Agente (Tempo)

Este é o modo como o agente opera ao longo do tempo. Esses princípios informam como projetamos agentes interagindo entre o passado, presente e futuro.

- **Passado**: Refletindo sobre a história que inclui estado e contexto.
  - O agente fornece resultados mais relevantes com base na análise de dados históricos mais ricos, além do evento, pessoas ou estados.
  - O agente cria conexões a partir de eventos passados e reflete ativamente na memória para interagir com situações atuais.
- **Agora**: Alertar mais do que notificar.
  - O agente incorpora uma abordagem abrangente para interagir com pessoas. Quando um evento acontece, o agente vai além de uma notificação estática ou outra formalidade estática. Ele pode simplificar fluxos ou gerar dinamicamente dicas para direcionar a atenção do usuário no momento certo.
  - O agente entrega informações com base no ambiente contextual, mudanças sociais e culturais e adaptadas à intenção do usuário.
  - A interação do agente pode ser gradual, evoluindo/crescendo em complexidade para capacitar os usuários ao longo do tempo.
- **Futuro**: Adaptar-se e evoluir.
  - O agente adapta-se a vários dispositivos, plataformas e modalidades.
  - O agente adapta-se ao comportamento do usuário, necessidades de acessibilidade e é livremente personalizável.
  - O agente é moldado e evolui por meio da interação contínua com o usuário.

### Agente (Núcleo)

Esses são os elementos-chave no núcleo do design de um agente.

- **Abraçar a incerteza, mas estabelecer confiança**.
  - Um certo nível de incerteza do agente é esperado. A incerteza é um elemento-chave do design de agentes.
  - Confiança e transparência são camadas fundamentais do design de agentes.
  - Os humanos têm controle sobre quando o agente está ligado/desligado e o status do agente é claramente visível o tempo todo.

## As Diretrizes para Implementar Esses Princípios

Ao utilizar os princípios de design anteriores, siga as seguintes diretrizes:

1. **Transparência**: Informe o usuário que a IA está envolvida, como ela funciona (incluindo ações passadas) e como fornecer feedback e modificar o sistema.
2. **Controle**: Permita que o usuário personalize, especifique preferências e personalize, e tenha controle sobre o sistema e seus atributos (incluindo a capacidade de esquecer).
3. **Consistência**: Busque experiências consistentes e multimodais entre dispositivos e pontos de acesso. Utilize elementos de UI/UX familiares sempre que possível (por exemplo, ícone de microfone para interação por voz) e reduza a carga cognitiva do cliente tanto quanto possível (por exemplo, respostas concisas, recursos visuais e conteúdo de "Saiba mais").

## Como projetar um agente de viagens usando esses princípios e diretrizes

Imagine que você está projetando um Agente de Viagens. Veja como você poderia pensar em usar os Princípios de Design e Diretrizes:

1. **Transparência** – Informe ao usuário que o Agente de Viagens é um agente habilitado por IA. Forneça algumas instruções básicas sobre como começar (por exemplo, uma mensagem de "Olá", exemplos de prompts). Documente isso claramente na página do produto. Mostre a lista de prompts que um usuário solicitou no passado. Deixe claro como fornecer feedback (botões de positivo e negativo, botão Enviar Feedback, etc.). Articule claramente se o agente tem restrições de uso ou de tópicos.
2. **Controle** – Certifique-se de que está claro como o usuário pode modificar o agente após ele ter sido criado, com coisas como o Prompt do Sistema. Permita que o usuário escolha o quão detalhado o agente deve ser, seu estilo de escrita e quaisquer restrições sobre o que o agente não deve abordar. Permita que o usuário visualize e exclua quaisquer arquivos ou dados associados, prompts e conversas anteriores.
3. **Consistência** – Certifique-se de que os ícones para Compartilhar Prompt, adicionar um arquivo ou foto e marcar alguém ou algo sejam padrão e reconhecíveis. Utilize o ícone de clipe de papel para indicar upload/compartilhamento de arquivos com o agente e um ícone de imagem para indicar upload de gráficos.

## Recursos adicionais

## Lição anterior

[Explorando Frameworks de Agentes](../02-explore-agentic-frameworks/README.md)

## Próxima lição

[Padrão de Design para Uso de Ferramentas](../04-tool-use/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.