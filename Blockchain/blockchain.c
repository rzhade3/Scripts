#include "blockchain.h"

Blockchain* blockchain;

/* Creates a new chain with the genesis block */
void new_chain() {
	blockchain = malloc(sizeof(Blockchain));
	if (!blockchain) {
		return NULL;
	}
	blockchain -> last_block = (Block*) new_genesis_block();
	blockchain -> size = 1;
}

/* Adds a new string to the chain */
void add_data(char* data) {
	Block* block = (Block*) new_block(data, blockchain -> last_block -> hash);
	block -> prev_block = blockchain -> last_block;
	blockchain -> last_block = block;
	blockchain -> size += 1;
}