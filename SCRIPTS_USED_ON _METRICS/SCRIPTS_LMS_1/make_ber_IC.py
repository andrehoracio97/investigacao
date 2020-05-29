#import sys
import os
import math
def compare_bits(compare,original):
	bit_errado=0
	
	temp=compare>>7
	temp_original=original>>7

	if temp&1 != temp_original&1:
		bit_errado=bit_errado+1;

	
	temp=compare>>6
	temp_original=original>>6

	if temp&1 != temp_original&1:
		bit_errado=bit_errado+1;

	temp=compare>>5
	temp_original=original>>5

	if temp&1 != temp_original&1:
		bit_errado=bit_errado+1;

	
	temp=compare>>4
	temp_original=original>>4

	if temp&1 != temp_original&1:
		bit_errado=bit_errado+1;

	temp=compare>>3
	temp_original=original>>3

	if temp&1 != temp_original&1:
		bit_errado=bit_errado+1;

	
	temp=compare>>2
	temp_original=original>>2

	if temp&1 != temp_original&1:
		bit_errado=bit_errado+1;

	temp=compare>>1
	temp_original=original>>1

	if temp&1 != temp_original&1:
		bit_errado=bit_errado+1;

	
	temp=compare>>0
	temp_original=original>>0

	if temp&1 != temp_original&1:
		bit_errado=bit_errado+1;


	return bit_errado



def read_file(file_or,file_test,num_packets, len_packet, janela_incrementar, array_pl, array_bler, array_ber):
	count_bit_error=0
	total_bytes_read=0


	count_num_packets=0
	count_packet_corr=0
	count_packet_error=0

	bits_error_one_byte=0
	flag=0; #flag if there is error in the packet

	janela_presente=janela_incrementar;



	compare = file_test.read(len_packet) #read 55 bytes
	original =file_or.read(len_packet) #read 55 bytes

	while compare:
		flag=0
		total_bytes_read=total_bytes_read+len_packet
		count_num_packets=count_num_packets+1

		for b in range(0,len(compare)):
			bits_error_one_byte=0#number bit errors in one byte
			bits_error_one_byte=compare_bits(compare[b],original[b])
			flag=flag+bits_error_one_byte
			count_bit_error=count_bit_error+bits_error_one_byte #count number of bit error on the byte


		compare = file_test.read(len_packet)
		original =file_or.read(len_packet)

		if flag==0:
			count_packet_corr=count_packet_corr+1
		else:
			count_packet_error=count_packet_error+1

		if count_num_packets>=janela_incrementar:
			print("-->Total Bytes Read: ",total_bytes_read)
			print("-->Pkt Received: ", count_num_packets,  "Pkt Correct: ", count_packet_corr, "Pkt Error: ", count_packet_error, "Bit Error: ", count_bit_error)
			pl=(num_packets-count_num_packets)/num_packets
			block_er= ((num_packets-count_num_packets)+count_packet_error)/num_packets

			ber=(count_bit_error/(count_num_packets*len_packet*8))
			print("-->Packet Loss: ", pl, "Block Error Rate: ",block_er, "Bit Error Rate: ", ber)

			array_pl.append(pl)
			array_bler.append(block_er)
			array_ber.append(ber)

			#Reset counters
			count_num_packets=0
			count_packet_corr=0
			count_packet_error=0

			bits_error_one_byte=0
			count_bit_error=0
			flag=0;

	return


def main():
	len_packet=55
	num_simulacoes=30
	num_packets=240000/num_simulacoes #8000 Pacotes

	nome_ficheiro="LMS82"
	tamanho_ficheiro_bob=os.path.getsize('/home/andre/ELI/'+nome_ficheiro+'/BOB_55_200000.txt')
	janela_bob=math.floor((tamanho_ficheiro_bob/len_packet)/num_simulacoes)
	print(janela_bob)

	tamanho_ficheiro_bob=os.path.getsize('/home/andre/ELI/'+nome_ficheiro+'/EVE_55_200000.txt')
	janela_eve=math.floor((tamanho_ficheiro_bob/len_packet)/num_simulacoes)
	print(janela_eve)



	#janela_bob=int(sys.argv[1])
	#janela_eve=int(sys.argv[2])

	total_bob_pl=[]
	total_bob_bler=[]
	total_bob_ber=[]

	total_eve_pl=[]
	total_eve_bler=[]
	total_eve_ber=[]

	'''temp_1=0 #pl
	temp_2=0 #bler
	temp_3=0 #ber

	temp_4=0 #num pkts received
	temp_5=0 #num pkts correct
	temp_6=0 #num pkts wrong
	temp_7=0 #num bit error

	total_pkts_received_b=0
	total_pkts_correct_b=0
	total_pkts_wrong_b=0
	total_bit_error_b=0

	total_pkts_received_e=0
	total_pkts_correct_e=0
	total_pkts_wrong_e=0
	total_bit_error_e=0
'''



	file_or = open("sequence55_240000.txt", "rb")
	print("Read Original!")
	#print("#######LEITURA THRESHOLD ->" + str(threshold) + " #######")

	name_file=nome_ficheiro+"/BOB_55_200000.txt"
	file_test = open(name_file, "rb")
	print("Read BOB!")
	read_file(file_or,file_test,num_packets,len_packet,janela_bob,total_bob_pl,total_bob_bler,total_bob_ber)


	file_test.close()
	file_or.close()

	file_or = open("sequence55_240000.txt", "rb")
	print("Read Original!")

	name_file=nome_ficheiro+"/EVE_55_200000.txt"
	file_test = open(name_file, "rb")
	print("Read EVE!")
	read_file(file_or,file_test,num_packets,len_packet,janela_eve,total_eve_pl,total_eve_bler,total_eve_ber)

	file_test.close()
	file_or.close()

	print("\n####################BOB###################")
	#print("-->Pkt Received: ", total_pkts_received_b,  "Pkt Correct: ", total_pkts_correct_b, "Pkt Error: ", total_pkts_wrong_b, "Bit Error: ", total_bit_error_b)

	#print("Total PL Bob:")
	print("\npl_b=", end = '')
	print(total_bob_pl) 

	#print("\nTotal BlER Bob:",)
	print("\nbler_b=", end = '')
	print(total_bob_bler) 

	#print("\nTotal BER Bob:")
	print("\nber_b=", end = '')
	print(total_bob_ber) 



	#print("\n####################EVE###################")
	#print("-->Pkt Received: ", total_pkts_received_e,  "Pkt Correct: ", total_pkts_correct_e, "Pkt Error: ", total_pkts_wrong_e, "Bit Error: ", total_bit_error_e)

	#print("Total PL Eve:")
	print("\npl_e=", end = '')
	print(total_eve_pl) 

	#print("\nTotal BlER Eve:")
	print("\nbler_e=", end = '')
	print(total_eve_bler) 

	#print("\nTotal BER Eve:")
	print("\nber_e=", end = '')
	print(total_eve_ber)









	'''
	file_or = open("original10000.txt", "rb")
	print("Read Original!")

	file_test = open("LMS10000_T4_1.txt", "rb")
	print("Read Test!")
	read_file(file_or,file_test)
	file_test.close()
	file_or.close()

	file_or = open("trasmit_1_mb.txt", "rb")
	print("Read Original!")

	file_test = open("S_LMS1MB_T4_2_CURENT.txt", "rb")
	print("Read Test!")

	read_file(file_or,file_test)
	file_test.close()
	file_or.close()'''


	'''threshold=0
	for threshold in range(1,2):
		file_or = open("original10000.txt", "rb")
		#print("Read Original!")

		print("#######LEITURA THRESHOLD ->" + str(threshold) + " #######")


		name_file="S_LMS10000_T"+str(threshold)+"_1.txt"
		file_test = open(name_file, "rb")
		#print("Read Test!")
		read_file(file_or,file_test)
		file_test.close()
		file_or.close()'''





if __name__== "__main__":
	main()
