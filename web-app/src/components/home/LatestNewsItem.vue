<template>
    <!-- Korišten je v-col zato što se ova komponenta ugniježđuje u v-row -->
    <v-col cols="12" sm="6" md="6" lg="4" xl="3">
        <v-card max-width="374" min-width="160" class="mx-auto">
            <v-img :src=post.img height="200px"  gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"  class="white--text align-end">
                <v-card-title
                    class="pt-0"
                >
                    {{ post.title }}
                </v-card-title>  
            </v-img>
            <v-card-text>
                {{ post.content }}
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                    text
                    :to="postLink"
                >
                    Više
                </v-btn>
            </v-card-actions>
        </v-card> 
    </v-col>
    
</template>

<script>
export default {
    name: "LatestNewsItem",
    props: {
        post: {type: Object, required: true}
    },
        computed: {
        postLink() {
            return {
                name: "post",
                params: {
                    id: this.post.id,
                    slug: "i-am-post-slug"
                    }
            }
        }
    }
}
</script>