import pandas as pd

df1=pd.read_csv('C:/Users/murruva/Desktop/carpeta trabajo SQL/TP-parte-2-python/ecommerce_customers_dataset.csv')
df2=pd.read_csv('C:/Users/murruva/Desktop/carpeta trabajo SQL/TP-parte-2-python/ecommerce_order_items_dataset.csv') 
df3=pd.read_csv('C:/Users/murruva/Desktop/carpeta trabajo SQL/TP-parte-2-python/ecommerce_order_payments_dataset.csv')
df4=pd.read_csv('C:/Users/murruva/Desktop/carpeta trabajo SQL/TP-parte-2-python/ecommerce_orders_dataset.csv')
df5=pd.read_csv('C:/Users/murruva/Desktop/carpeta trabajo SQL/TP-parte-2-python/ecommerce_products_dataset.csv')

df1.set_index('customer_id', inplace=True)
df2.set_index('order_id', inplace=True)
df3.set_index('order_id', inplace=True)
df4.set_index('order_id', inplace=True)
df5.set_index('product_id', inplace=True)

cliente_unico = df1['customer_unique_id'].nunique()#devuelve el nro valores unicos
print (f'la cantidad total de clientes unicos:{cliente_unico}')

promedio_pago = df3['payment_value'].mean()#devuelve el nro valores unicos
print (f'la cantidad total de pago: {promedio_pago}') 

mas_vendido = df5['product_category_name'].value_counts()#devuelve el nro valores unicos
la_mas_repetida = mas_vendido.idxmax()#devuelve el nro valores unicos
print (f'cantidad mas vendida: {la_mas_repetida}')

pedidos_realizados = len(df4)
print (f'lo mas pedido: {pedidos_realizados}')