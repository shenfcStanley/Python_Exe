import pickle

def my_function():
  

  data = b'\x80\x04\x95-\x18\.' ## binary data could be generated by 'data = pickle.dumps(model_file)'

  model = pickle.loads(data)
