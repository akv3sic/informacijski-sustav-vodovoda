<template>
    <div>
        <Header />
        <v-container :class="{'pa-16': $vuetify.breakpoint.lgAndUp, 'pa-4': $vuetify.breakpoint.md,}">
            <HeadingWithImage title="Novosti" height="18vh"/>
            <v-container class="mt-2">
                <v-row>
                    <v-col class="d-flex align-center justify-center">
                        <v-text-field
                            placeholder="Pretražite blog..."
                        >
                             <v-icon
                                slot="append"
                                color="secondary"
                                >
                                mdi-magnify
                                </v-icon>
                        </v-text-field>
                    </v-col>
                </v-row>

                <!-- OBJAVE -->
                <HorizontalPost 
                    v-for="post in posts"
                    :key="post.id"
                    :title=post.title
                    :content=post.content
                    published="12. 1. 2021. 14:54"
                    imgSrc="https://www.blogtyrant.com/wp-content/uploads/2017/02/how-to-write-a-good-blog-post.png"
                />            
            </v-container>

            <!-- Straničenje -->
            <v-row>
                <v-col class="text-center">
                    <v-pagination
                    :length="3"
                    disabled
                    ></v-pagination>
                </v-col>
            </v-row>

        </v-container>
        
    </div>
</template>

<script>
import Header from "@/components/layout/TheHeader"
import HeadingWithImage from "@/components/layout/HeadingWithImage"
import HorizontalPost from "@/components/blog/HorizontalPost"

export default {
    name: "Posts",
    components: { Header, HeadingWithImage, HorizontalPost },
    data: () => ({
        posts: [
            {id: 1, title:"Post title", content: "Adipiscing elit duis tristique sollicitudin nibh. Sed faucibus turpis in eu mi bibendum. Viverra orci sagittis eu volutpat odio facilisis mauris sit amet. Eu non diam phasellus vestibulum lorem sed. Maecenas volutpat blandit aliquam etiam erat velit.", img: "https://www.blogtyrant.com/wp-content/uploads/2017/02/how-to-write-a-good-blog-post.png"}, 
            {id: 2, title:"Post title", content: "Adipiscing elit duis tristique sollicitudin nibh. Sed faucibus turpis in eu mi bibendum. Viverra orci sagittis eu volutpat odio facilisis mauris sit amet. Eu non diam phasellus vestibulum lorem sed. Maecenas volutpat blandit aliquam etiam erat velit.", img : "https://www.blogtyrant.com/wp-content/uploads/2017/02/how-to-write-a-good-blog-post.png"}, 
            {id: 3, title:"Post title", content: "Adipiscing elit duis tristique sollicitudin nibh. Sed faucibus turpis in eu mi bibendum. Viverra orci sagittis eu volutpat odio facilisis mauris sit amet. Eu non diam phasellus vestibulum lorem sed. Maecenas volutpat blandit aliquam etiam erat velit.", img : "https://www.blogtyrant.com/wp-content/uploads/2017/02/how-to-write-a-good-blog-post.png"}, 
            {id: 4, title:"Post title", content: "Adipiscing elit duis tristique sollicitudin nibh. Sed faucibus turpis in eu mi bibendum. Viverra orci sagittis eu volutpat odio facilisis mauris sit amet. Eu non diam phasellus vestibulum lorem sed. Maecenas volutpat blandit aliquam etiam erat velit.", img: "https://www.blogtyrant.com/wp-content/uploads/2017/02/how-to-write-a-good-blog-post.png"}       
            ]
    })    
}
</script>

<style>

</style>