import Content from './content.js'
import Link from 'next/link'

export default function App() {
    
    return (
        <>
            <h1>hello world</h1>
            <Link href="/chat">Chat</Link>
            <Content/>
        </>
    )
}