m = {'id': 'chatcmpl-6smZFlJUSpEaQifNL9yV2lfZ0hTFP', 'object': 'chat.completion', 'created': 1678514425, 'model': 'gpt-3.5-turbo-0301', 'usage': {'prompt_tokens': 9, 'completion_tokens': 12, 'total_tokens': 21}, 'choices': [{'message': {'role': 'assistant', 'content': '\n\nHello there! How can I assist you today?'}, 'finish_reason': 'stop', 'index': 0}]}
print(m)
print(m['choices'][0]['message']['content'])