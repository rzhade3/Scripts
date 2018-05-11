#include "block.h"
#include <stdlib.h>

block_t* create_genesis_block() {
	block_t* genesis_block;
	genesis_block = (block_t*) malloc(sizeof(block_t));
	if (genesis_block == NULL) {
		exit(1);
	}
	genesis_block -> index = 0;
	genesis_block -> timestamp = time(0);
	genesis_block -> data = "hello you silly billy";
	return genesis_block;
}

block_t* new_block(char* data) {
	block_t* block = malloc(sizeof(block_t));
	block -> timestamp = time(0);
	block -> data = data;
	return block;
}

void calculate_hash(block_t* block) {
	block -> hash = 7890;
}
