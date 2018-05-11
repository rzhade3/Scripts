#include "queue.h"
#include <stdint.h>

typedef struct blockchain_t {
	block_t* genesis_block;
	uint8_t size;
	uint8_t difficulty;
	uint8_t mining_reward;
	queue_t* unconfirmed_transactions;
} blockchain_t;

// Initializes blockchain with some initial memory
void init_blockchain(void);

// Adds a new block to the blockchain
void add_block(char* data);

// Frees up any memory used by the blockchain
void clean_data(void);

void mine_block(block_t* block);
