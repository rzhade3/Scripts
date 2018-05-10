#include "blockchain.h"
#include <stdlib.h>

blockchain_t* blockchain;

void init() {
	blockchain = (blockchain_t*) malloc(sizeof(blockchain_t));
	if (blockchain == NULL) {
		exit(1);
	}
	blockchain -> genesis_block = create_genesis_block();
}

void add_block(char* data) {
	block_t* n_block = (block_t*) new_block(data);
}

void clean_data() {
	
}

