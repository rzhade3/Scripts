#include "block.h"
#include <stdint.h>

typedef struct blockchain_t {
	block_t* genesis_block;
	uint8_t size;
	uint8_t difficulty;
	uint8_t mining_reward;
} blockchain_t;

void init(void);

void add_block(char* data);

void clean_data(void);
