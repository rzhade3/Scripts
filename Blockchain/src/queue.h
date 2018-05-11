#include "block.h"
#include <stdlib.h>

typedef struct queue_t {
	block_t* head;
	block_t* tail;
} queue_t;

// Initializes the queue with memory space, and zeroes it out
void init_queue(queue_t* queue);

// Pushes a block onto the queue
void push(queue_t* queue, block_t* block);

// Removes the first item added to the queue
block_t* pop(queue_t* queue);

// Looks at the first item added to the queue
block_t* peek(queue_t* queue);
