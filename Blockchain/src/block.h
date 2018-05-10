#include <time.h>
#include <stdint.h>

typedef struct block_t {
	uint8_t index;
	uint16_t previousHash;
	uint16_t hash;
	uint8_t nonce;
	uint16_t timestamp;
	char* data;
} block_t;

block_t* create_genesis_block(void);

block_t* new_block(char* data);

void mine_block(block_t* block);
