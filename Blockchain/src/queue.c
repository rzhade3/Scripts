#include "queue.h"
#include <stdio.h>
#include <string.h>

void init_queue(queue_t* queue) {
	queue = malloc(sizeof(queue_t));
	if (queue == NULL) {
		exit(1);
	}
	memset(queue, 0, sizeof(queue_t));
}

void push(queue_t* queue, block_t* block) {
	if (queue -> head == NULL) {
		queue -> head = block;
		queue -> tail = block;
	} else {
		queue -> tail -> next = block;
	}
}

block_t* pop(queue_t* queue) {
	if (queue -> head == NULL) {
		printf("No unconfirmed transactions at this time\n");
		return NULL;
	}
	block_t* ret = queue -> head;
	queue -> head = queue -> head -> next;
	return ret;

}

block_t* peek(queue_t* queue) {
	return queue -> head;
}
