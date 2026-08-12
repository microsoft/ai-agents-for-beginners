[![Como Desenhar Bons Agentes de IA](../../../translated_images/pt-PT/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Clique na imagem acima para ver o vídeo desta lição)_
# Princípios de Design de Agentes de IA

## Introdução

Existem muitas formas de pensar na construção de Sistemas Agentes de IA. Dado que a ambiguidade é uma característica e não um defeito no design de IA Generativa, por vezes é difícil para os engenheiros descobrirem por onde começar. Criámos um conjunto de Princípios de Design UX centrados no ser humano para permitir que os desenvolvedores construam sistemas agentes centrados no cliente para resolver as necessidades do seu negócio. Estes princípios de design não são uma arquitetura prescritiva, mas sim um ponto de partida para as equipas que estão a definir e a desenvolver experiências agentes.

Em geral, os agentes devem:

- Ampliar e escalar as capacidades humanas (brainstorming, resolução de problemas, automação, etc.)
- Preencher lacunas de conhecimento (atualizar-me em domínios de conhecimento, tradução, etc.)
- Facilitar e apoiar a colaboração nas formas que preferimos trabalhar com outros enquanto indivíduos
- Tornar-nos melhores versões de nós mesmos (por exemplo, treinador de vida/gestor de tarefas, ajudando-nos a aprender regulação emocional e técnicas de mindfulness, construir resiliência, etc.)

## Esta Lição Vai Cobrir

- O que são os Princípios de Design Agente
- Quais são as orientações a seguir ao implementar estes princípios de design
- Quais são alguns exemplos de utilização dos princípios de design

## Objetivos de Aprendizagem

Depois de completar esta lição, será capaz de:

1. Explicar o que são os Princípios de Design Agente
2. Explicar as orientações para usar os Princípios de Design Agente
3. Compreender como construir um agente usando os Princípios de Design Agente

## Os Princípios de Design Agente

![Princípios de Design Agente](../../../translated_images/pt-PT/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agente (Espaço)

Este é o ambiente em que o agente opera. Estes princípios informam como desenhamos agentes para interagir nos mundos físico e digital.

- **Conectar, não colapsar** – ajudar a conectar pessoas a outras pessoas, eventos e conhecimento acionável para permitir colaboração e ligação.
- Os agentes ajudam a conectar eventos, conhecimento e pessoas.
- Os agentes aproximam as pessoas. Não são projetados para substituir ou diminuir as pessoas.
- **Facilmente acessível, mas ocasionalmente invisível** – o agente opera em grande parte em segundo plano e só nos alerta quando é relevante e apropriado.
  - O agente é facilmente descoberto e acessível para utilizadores autorizados em qualquer dispositivo ou plataforma.
  - O agente suporta entradas e saídas multimodais (som, voz, texto, etc.).
  - O agente pode transitar sem dificuldades entre primeiro plano e segundo plano; entre proativo e reativo, dependendo da perceção das necessidades do utilizador.
  - O agente pode operar de forma invisível, mas o seu processo de fundo e colaboração com outros agentes é transparente e controlável pelo utilizador.

### Agente (Tempo)

É assim que o agente opera ao longo do tempo. Estes princípios informam como desenhamos agentes que interagem no passado, presente e futuro.

- **Passado**: Refletindo sobre a história que inclui tanto estado como contexto.
  - O agente fornece resultados mais relevantes baseados na análise de dados históricos mais ricos para além do evento, pessoas ou estados.
  - O agente cria conexões a partir de eventos passados e reflete ativamente na memória para interagir com situações atuais.
- **Agora**: Incentivando mais do que notificando.
  - O agente incorpora uma abordagem abrangente para interagir com pessoas. Quando um evento acontece, o agente vai além da notificação estática ou qualquer outra formalidade estática. O agente pode simplificar fluxos ou gerar dinamicamente sinais para direcionar a atenção do utilizador no momento certo.
  - O agente fornece informação baseada no ambiente contextual, mudanças sociais e culturais e adaptadas à intenção do utilizador.
  - A interação com o agente pode ser gradual, evoluindo e crescendo em complexidade para capacitar os utilizadores a longo prazo.
- **Futuro**: Adaptando e evoluindo.
  - O agente adapta-se a vários dispositivos, plataformas e modalidades.
  - O agente adapta-se ao comportamento do utilizador, necessidades de acessibilidade e é livremente personalizável.
  - O agente é moldado por e evolui através da interação contínua com o utilizador.

### Agente (Núcleo)

Estes são os elementos-chave no núcleo do design de um agente.

- **Aceitar a incerteza mas estabelecer confiança**.
  - Um certo nível de incerteza do agente é esperado. A incerteza é um elemento chave do design do agente.
  - Confiança e transparência são camadas fundamentais do design do agente.
  - Os humanos controlam quando o agente está ligado/desligado e o estado do agente é claramente visível em todos os momentos.

## As Orientações para Implementar Estes Princípios

Quando estiver a usar os princípios de design anteriores, use as seguintes orientações:

1. **Transparência**: Informe o utilizador de que a IA está envolvida, como funciona (incluindo ações passadas), e como dar feedback e modificar o sistema.
2. **Controlo**: Permita que o utilizador personalize, especifique preferências e personalize, e tenha controlo sobre o sistema e seus atributos (incluindo a capacidade de esquecer).
3. **Consistência**: Procure experiências consistentes multimodais em dispositivos e pontos finais. Utilize elementos UI/UX familiares sempre que possível (por exemplo, ícone de microfone para interação por voz) e reduza ao máximo a carga cognitiva do cliente (por exemplo, respostas concisas, ajudas visuais e conteúdos ‘Saber Mais’).

## Como Desenhar um Agente de Viagens usando Estes Princípios e Orientações

Imagine que está a desenhar um Agente de Viagens, aqui está como poderia pensar em usar os Princípios e Orientações de Design:

1. **Transparência** – Informe o utilizador de que o Agente de Viagens é um Agente habilitado por IA. Forneça algumas instruções básicas sobre como começar (por exemplo, uma mensagem “Olá”, exemplos de comandos). Documente claramente isto na página do produto. Mostre a lista de comandos que um utilizador já pediu no passado. Deixe claro como dar feedback (polegares para cima e para baixo, botão Enviar Feedback, etc.). Articule claramente se o Agente possui restrições de uso ou temas.
2. **Controlo** – Certifique-se de que é claro como o utilizador pode modificar o agente depois de criado, com coisas como o Pedido de Sistema. Permita que o utilizador escolha quão detalhado o agente deve ser, seu estilo de escrita, e quaisquer alertas sobre o que o agente não deve falar. Permita que o utilizador visualize e apague quaisquer ficheiros ou dados associados, comandos e conversas passadas.
3. **Consistência** – Certifique-se que os ícones para Partilhar Comando, adicionar ficheiro ou foto e marcar alguém ou algo são padrão e reconhecíveis. Use o ícone de clipe para indicar envio/partilha de ficheiros com o Agente, e o ícone de imagem para indicar envio de gráficos.

## Exemplos de Código

- Python: [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/03-dotnet-agent-framework.md)


## Tem Mais Perguntas sobre Padrões de Design de Agentes de IA?

Junte-se ao [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) para conhecer outros aprendizes, assistir horas de atendimento e esclarecer as suas dúvidas sobre Agentes de IA.

## Recursos Adicionais

- <a href="https://openai.com" target="_blank">Práticas para Governar Sistemas Agentes de IA | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">Projeto HAX Toolkit - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Caixa de Ferramentas de IA Responsável</a>

## Lição Anterior

[Explorando Estruturas Agentes](../02-explore-agentic-frameworks/README.md)

## Próxima Lição

[Padrão de Design para Uso de Ferramentas](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->