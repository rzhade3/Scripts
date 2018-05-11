#include "blockchain.h"
#include <stdlib.h>

blockchain_t* blockchain;

void init_blockchain() {
	blockchain = (blockchain_t*) malloc(sizeof(blockchain_t));
	if (blockchain == NULL) {
		exit(1);
	}
	init_queue(blockchain -> unconfirmed_transactions);
	blockchain -> mining_reward = 10;
	blockchain -> difficulty = 2;
	blockchain -> genesis_block = create_genesis_block();
}

void add_block(char* data) {
	block_t* block = (block_t*) new_block(data);
	if (block == NULL) {
		exit(1);
	}
	block -> data = data;
	push(blockchain -> unconfirmed_transactions, block);
}

void clean_data() {
	
}

void mine_block(block_t* block) {
	while ((block -> hash) >> (16 - blockchain -> difficulty) != 0) {
		block -> nonce++;
		calculate_hash(block);
	}
	// Iterating to the back of the blockchain to add it
}
