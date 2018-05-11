#include <time.h>
#include <stdint.h>

typedef struct block_t {
	uint8_t index;
	struct block_t* next;
	uint16_t hash;
	uint8_t nonce;
	uint16_t timestamp;
	char* data;
} block_t;

// Generate genesis block
block_t* create_genesis_block(void);

// Creates a new block given some data
block_t* new_block(char* data);

// Calculates the hash for the block, using timestamp, data and nonce
void calculate_hash(block_t* block);
