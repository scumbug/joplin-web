<template>
    <div>
    <div v-if="note.todo_completed === 0 && note.todo_due === 0" class="card text-primary">
        <div class="card-body">
            <p class="card-text">{{ note.title }}</p>
            <p class="card-text">
                <small class="text-muted">created: {{ moment(note.created_time).format('lll') }}</small>
                <small v-if="note.todo_due > 0" class="text-muted"> due: {{ moment(note.todo_due).format('lll') }}</small>
            </p>
        </div>
    </div>
    <div v-else-if="note.todo_completed === 1" class="card text-success">
        <div class="card-body">
            <p class="card-text">{{ note.title }}</p>
            <p class="card-text">
                <small class="text-muted">created: {{ moment(note.created_time).format('lll') }}</small>
                <small v-if="note.todo_due > 0" class="text-muted"> due: {{ moment(note.todo_due).format('lll') }}</small>
            </p>
        </div>
    </div>
    <div v-else class="card text-warning">
        <div class="card-body">
            <p class="card-text">{{ note.title }}</p>
            <p class="card-text">
                <small class="text-muted">created: {{ moment(note.created_time).format('lll') }}</small>
                <small v-if="note.todo_due > 0" class="text-muted"> due: {{ moment(note.todo_due).format('lll') }}</small>
            </p>
        </div>
    </div>
    </div>
</template>

<script>
export default {
  props: ['note']
}
</script>
