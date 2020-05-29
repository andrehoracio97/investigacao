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



def read_file(file_or,file_test,num_packets, len_packet):
	count_bit_error=0
	total_bytes_read=0


	count_num_packets=0
	count_packet_corr=0
	count_packet_error=0

	bits_error_one_byte=0
	flag=0; #flag if there is error in the packet



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

	
	print("-->Total Bytes Read: ",total_bytes_read)
	print("-->Pkt Received: ", count_num_packets,  "Pkt Correct: ", count_packet_corr, "Pkt Error: ", count_packet_error, "Bit Error: ", count_bit_error)
	pl=(num_packets-count_num_packets)/num_packets
	block_er= ((num_packets-count_num_packets)+count_packet_error)/num_packets
	try:
		ber=(count_bit_error/(count_num_packets*len_packet*8))
	except Exception as e:
		ber=0
	finally:
		pass
	print("-->Packet Loss: ", pl, "Block Error Rate: ",block_er, "Bit Error Rate: ", ber)
	#print("Count Packet Corr: ",count_packet_corr)
	#print("Count Packet Error: ",count_packet_error)
	#print("Count Bit Error: ",count_bit_error)

	return pl,block_er,ber


def main():
	num_packets=240000
	len_packet=55
	num_simulacoes=1

	nome_ficheiro="LMS82"

	file_or = open("sequence55_240000.txt", "rb")
	print("Read Original!")

	file_test = open(nome_ficheiro+"/BOB_55_200000.txt", "rb")
	print("Read Test!")
	read_file(file_or,file_test,num_packets,len_packet)
	file_test.close()
	file_or.close()

	file_or = open("sequence55_240000.txt", "rb")
	print("Read Original!")

	file_test = open(nome_ficheiro+"/EVE_55_200000.txt", "rb")
	print("Read Test!")
	read_file(file_or,file_test,num_packets,len_packet)
	file_test.close()
	file_or.close()










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
