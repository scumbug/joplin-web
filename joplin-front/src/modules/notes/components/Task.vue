<template>
    <div>
        <b-card :title="note.title" v-if="note.todo_completed === 0 && note.todo_due === 0"  border-variant="light">
            <p class="card-text">
                <small class="text-muted">created: {{ moment(note.created_time).format('lll') }}</small>
                <small v-if="note.todo_due > 0" class="text-muted"> due: {{ moment(note.todo_due).format('lll') }}</small>
            </p>
        </b-card>

        <b-card :title="note.title" v-else-if="note.todo_completed === 1"  border-variant="success">
            <p class="card-text">
                <small class="text-muted">created: {{ moment(note.created_time).format('lll') }}</small>
                <small v-if="note.todo_due > 0" class="text-muted"> due: {{ moment(note.todo_due).format('lll') }}</small>
            </p>
        </b-card>
        <b-card :title="note.title" v-else border-variant="warning">
            <p class="card-text">
                <small class="text-muted">created: {{ moment(note.created_time).format('lll') }}</small>
                <small v-if="note.todo_due > 0" class="text-muted"> due: {{ moment(note.todo_due).format('lll') }}</small>
            </p>
        </b-card>
    </div>
</template>

<script>
export default {
  props: ['note']
}
</script>
