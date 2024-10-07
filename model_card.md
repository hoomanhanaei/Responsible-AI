# Model card for "C4AI Command R+"

Jump to section:

- [Model overview](#model-overview)
- [Intended use](#intended-use)
- [Factors](#factors)
- [Metrics](#metrics)
- [Evaluation data](#evaluation-data)
- [Training data](#training-data)
- [Quantitative analyses](#quantitative-analyses)
- [Ethical considerations](#ethical-considerations)
- [Caveats and recommendations](#caveats-and-recommendations)

## Model overview
- **C4AI Command R+:**<br> is an open weights research release of a 104 billion parameter large language model (LLM) designed for advanced natural language processing (NLP) tasks, and is also part of a family of open weight releases from Cohere For AI and Cohere.<br>It is Built on the transformer architecture, this model excels in text understanding, generation, and other complex (NLP) tasks. Its large parameter size allows it to capture more nuanced relationships and patterns within text, making it powerful for tasks requiring high levels of comprehension and fluency ([more](https://huggingface.co/CohereForAI/c4ai-command-r-plus-4bit)).

- **This Model performs:**<br> various natural language processing (NLP) tasks, including text generation, summarization, translation, and question answering. Its architecture allows it to understand and generate human-like text based on the context provided, making it suitable for a range of applications in conversational AI, content creation.

- **Intended Use Cases:**<br>Generate text and code: Use the model’s grounded generation capabilities to generate text and code based on a list of supplied document snippets.<br>Automate complex tasks: Use the model’s tool use and multihop capabilities to automate complex tasks that require multiple steps.<br>Improve your language understanding: Use the model’s multilingual support to improve your language understanding and respond to users in different languages ([Use-cases](https://dataloop.ai/library/model/cohereforai_c4ai-command-r-plus-4bit/)).

- **Potential missuses:**<br>Reduced Censorship on NSFW Conten makes Command R+ capable of handling NSFW storytelling with less resistance, providing responses readily in these contexts. This increased flexibility could be exploited to generate inappropriate or harmful content ([NSFW and Censorship](https://llm.extractum.io/static/blog/?id=command-r-plus-discussions)).

