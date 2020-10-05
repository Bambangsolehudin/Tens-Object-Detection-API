#untuk path
import os
#untuk ambil ekstensi
import glob
#untuk dataframe mengubah data dr file ke table
import pandas as pd
#untuk tree xml
import xml.etree.ElementTree as ET
#function beserta nilai parameter path
def xml_to_csv(path):
	#isi array kosong dengan variabel
    xml_list = []
	#ambil seluruh data ekstensi xml
    for xml_file in glob.glob(path + '/*.xml'):
	#mengambil isi data dr tree per xml
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
			#mndapatkan file name
            value = (root.find('filename').text,
			#menemukan ukuran dan bbox
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
					#menambah value pada array xml_list
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
	#isi dari tabel mengubah seluruh xml menjadi tabel csv melalui dataframe 
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df
def main():
    for directory in ['train', 'test']:
        image_path = os.path.join(os.getcwd(), 'Annotation/{}'.format(directory))
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv('Data/{}_labels.csv'.format(directory), index=None)
        print('Successfully converted xml to csv.')
main()