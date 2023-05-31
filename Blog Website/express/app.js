const express=require('express')
const app=express()
const mongoose=require('mongoose')
const blogRoutes=require('./routes/blogRoutes')

const dburi='mongodb+srv://saisravanikota:sravani@Cluster0.aezngbp.mongodb.net/';
mongoose.connect(dburi,{useNewUrlParser: true, useUnifiedTopology: true})
    .then((result)=>app.listen(5000))
    .catch((err)=>console.log(err))


app.use(express.urlencoded({extended: true}))
app.set('view engine', 'ejs');

app.get('/add-blog',(req,res)=>{
    const blog=new Blog({
        title: 'new blog 1',
        snippet: 'about my new blog',
        body: 'more about my new blog'
    })
    blog.save()
        .then((result)=>{
            res.send(result)  
        })
        .catch((err)=>{
            console.log(err)
        })
})

app.get('/all-blogs',(req,res)=>{
    Blog.find()
        .then((result)=>{
            res.send(result)
        })
        .catch((err)=>{
            console.log(err)
        })
})

app.get('/single-blog',(req,res)=>{
    Blog.findById('64673471be8874bd32f227ba')
        .then((result)=>{
            res.send(result)
        })
        .catch((err)=>{
            console.log(err)
        })
})

app.get('/',(req,res)=>{
    res.redirect('/blogs')
})

app.get('/about',(req,res)=>{
    res.render('about',{title:'About'})
})

app.get('/create',(req,res)=>{
    res.render('create',{title:'Create'})
})

app.use('/blogs', blogRoutes)


app.use((req,res)=>{
    res.render('404',{title:'404'})
})
