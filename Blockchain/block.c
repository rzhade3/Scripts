#include "blockchain.h"
#include <time.h>
#include <string.h>

/* Sets the hash for the block using the data string */
void set_hash(Block* block) {
    uint8_t hash[32];
    calc_sha_256(hash, block -> data, strlen(block -> data));
    block -> hash = hash;
}

/* Returns a new block with all of the given data and the current timestamp */
void* new_block(char *data, char *prevHash) {
    Block* block = (Block*) malloc(sizeof(Block));
    if (!block) {
        return NULL;
    }
    block -> timestamp = (int) time(NULL);
    block -> data = data;
    block -> previous_hash = prevHash;
    set_hash(block);
    return block;
}

/* Returns a new genesis block, with no previous block */
void* new_genesis_block() {
    Block* gen_block = (Block*) malloc(sizeof(Block));
    if (!gen_block) {
        return NULL;
    }
    gen_block -> timestamp = (int) time(NULL);
    gen_block -> data = "Hello world";
    set_hash(gen_block);
    return (void*) gen_block;
}

