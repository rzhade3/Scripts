#include <stdlib.h>
// Structs
typedef struct Block64 {
	int timestamp;
	char* data;
	char* previous_hash;
	char* hash;
	void* prev_block;
} Block;

typedef struct Blockchain64 {
	Block* last_block;
	int size;
} Blockchain;

// Function prototypes
void calc_sha_256(uint8_t hash[32], const void *input, size_t len);

void setHash(Block *block);

void* new_block(char *data, char* prevHash);

void* new_genesis_block();

void new_chain();

void add_data(char* data);
