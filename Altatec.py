import streamlit as st
from PIL import Image 



image = Image.open('ig.jpg')
st.image(image, width=300)
st.title('Alta Tec')
   
     
#inputs
#porcentagem_racao=0.003

taxa_sobrev_despeca= 85 #   despesca---porcentagem
area = st.number_input( "Informe a Área da lamina d'agua total da propriedade", step=1  )#ha
densidade = st.number_input('Qual densidade de estocagem?', step=1) #individuos/m2
peso_mediog= st.number_input('Qual peso medio desejado')#g
taxa_sobrevivencia=59 #berçario------porcentagem
fca= 2.5
preco_racao=4.5
preco_camarao= 29
preco_mil_pl= 9
#calculos

area_m2= area*10000
povoamento= densidade*area_m2 
sobrev_despesca= ((povoamento*taxa_sobrev_despeca)/100)
peso_mediokg= peso_mediog/1000
biomassa= peso_mediokg*sobrev_despesca
larva_total= (povoamento)/(taxa_sobrevivencia/100)
mortalidade= larva_total-povoamento
racao= biomassa*fca
gasto_racao= racao*preco_racao
gasto_pl=preco_mil_pl*larva_total/1000

lucroB= biomassa*preco_camarao
lucroL= lucroB-(gasto_pl+gasto_racao)
tx_ra = f'R${gasto_racao:_.2f}'
tx_ra = tx_ra.replace('.',',').replace('_','.')
tx_lucroB = f'R${lucroB:_.2f}'
tx_lucroB = tx_lucroB.replace('.',',').replace('_','.')
tx_lucroL = f'R${lucroL:_.2f}'
tx_lucroL = tx_lucroL.replace('.',',').replace('_','.')
#saidas
#print(f'larvas necessarias{larva_total}'

if peso_mediog > 0 :
    st.write(f'Povoamneto: {povoamento} individuos necessarios')
    st.write(f'Área: {area_m2} area total de lamina dagua')
    st.write(f'Larvas necessarias: {int(larva_total)} pl necessarias no berçario')
    st.write(f'Mortalidade: {int(mortalidade)} número de individuos que morreram')
    st.write(f'Sobrevivencia despesca: {int(sobrev_despesca)} individuos')
    st.write(f'Ração: {racao} kg de ração')
    st.write(f'Biomassa: {(biomassa)} kg')
    st.write(f'Gasto pl: R${round(gasto_pl,2)} ')
    st.write(f'Custo ração: {tx_ra} ')
    st.write(f'Lucro bruto: {tx_lucroB} ')
    st.write(f'Lucro liquido: {tx_lucroL} ')
