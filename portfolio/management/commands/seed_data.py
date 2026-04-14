from django.core.management.base import BaseCommand
from portfolio.models import PortfolioItem


class Command(BaseCommand):
    help = 'Seed the database with Yogesh Gaikwad portfolio data'

    def handle(self, *args, **options):
        # Clear existing data
        PortfolioItem.objects.all().delete()
        self.stdout.write('Cleared existing portfolio items...')

        items = [
            # Profile
            {
                'category': 'profile',
                'title': 'Yogesh Gaikwad',
                'subtitle': 'Software Engineer | Distributed Systems | Backend Infrastructure',
                'description': '''
                    <p class="mb-2">📍 Dublin, Ireland</p>
                    <p class="mb-2">📧 imyogeshgaikwad@gmail.com</p>
                    <p class="mb-2">📱 +353 87 492 5777</p>
                    <p class="mb-2">🛂 Stamp 1G — Available Immediately</p>

                    <p class="mt-4 leading-relaxed">
                        Software Engineer with production experience building distributed systems, high-availability APIs,
                        and event-driven microservices architectures serving 50,000+ users across telecom and digital
                        platforms at Tata Communications and Tata Elxsi. Proven track record of reducing system latency
                        by 45%, cutting infrastructure costs by 25%, and improving deployment velocity by 80%.
                        Deep expertise in Node.js, TypeScript, Python, and AWS cloud-native infrastructure.
                        Architect of fault-tolerant systems operating at 99.9% uptime under enterprise workloads.
                    </p>
                ''',
                'order': 1,
            },

            # Education
            {
                'category': 'education',
                'title': 'M.Sc. Information Systems with Computing',
                'subtitle': 'Dublin Business School (DBS), Ireland — First Class Honours',
                'description': '''
                    <p class="mb-2">Graduating February 2026.</p>
                    <p class="mb-2"><strong>Core Modules:</strong></p>
                    <ul class="list-disc list-inside space-y-1">
                        <li>Distributed Systems</li>
                        <li>Cloud Architecture</li>
                        <li>Scalable Computing</li>
                        <li>Database Engineering</li>
                        <li>Software Design Patterns</li>
                    </ul>
                ''',
                'date_start': 'Apr 2024',
                'date_end': 'Feb 2026',
                'order': 1,
            },
            {
                'category': 'education',
                'title': 'Bachelor of Technology in Information Technology',
                'subtitle': 'SVKM Institute of Technology, India — First Class Honours',
                'description': '''
                    <p class="mb-2"><strong>Core Modules:</strong></p>
                    <ul class="list-disc list-inside space-y-1">
                        <li>Data Structures &amp; Algorithms</li>
                        <li>Operating Systems</li>
                        <li>Computer Networks</li>
                        <li>Database Management Systems</li>
                        <li>Object-Oriented Programming</li>
                    </ul>
                ''',
                'date_start': 'Jun 2018',
                'date_end': 'May 2022',
                'order': 2,
            },

            # Experience
            {
                'category': 'experience',
                'title': 'Software Engineer',
                'subtitle': 'Tata Communications',
                'description': '''
                    <ul class="list-disc list-inside space-y-2">
                        <li>Designed and deployed scalable REST APIs handling <span class="text-green-400 font-bold">25,000+ daily requests</span>, improving average response time by <span class="text-green-400 font-bold">40%</span> (500ms → 300ms) through query optimisation and Redis caching.</li>
                        <li>Architected event-driven background job processing system using message queues and worker services, improving system throughput by <span class="text-green-400 font-bold">60%</span> under peak load for 50,000+ enterprise users.</li>
                        <li>Implemented horizontal scaling across containerised services using Docker and AWS EC2 auto-scaling groups, achieving <span class="text-green-400 font-bold">99.9% uptime</span> SLA for Fortune 500 clients.</li>
                        <li>Optimised PostgreSQL queries across <span class="text-blue-400 font-bold">10M+ records</span>, reducing critical query latency from 850ms to 300ms (<span class="text-green-400 font-bold">65% reduction</span>), eliminating report timeout issues for 3 downstream teams.</li>
                        <li>Built end-to-end CI/CD pipeline with GitHub Actions, cutting deployment cycles from 2 hours to 20 minutes (<span class="text-green-400 font-bold">83% reduction</span>) across 4 engineering teams.</li>
                        <li>Instrumented production systems with CloudWatch metrics and centralised log aggregation, reducing MTTR by <span class="text-green-400 font-bold">35%</span> and enabling proactive incident detection.</li>
                    </ul>
                ''',
                'date_start': 'Jul 2022',
                'date_end': 'Aug 2024',
                'technologies': 'Node.js, TypeScript, Python, REST APIs, Redis, PostgreSQL, Docker, AWS (EC2, S3, Lambda, CloudWatch), GitHub Actions, CI/CD, Message Queues',
                'order': 1,
            },
            {
                'category': 'experience',
                'title': 'Software Engineer (Internship)',
                'subtitle': 'Tata Elxsi',
                'description': '''
                    <ul class="list-disc list-inside space-y-2">
                        <li>Engineered modular microservices architecture for digital product platforms supporting <span class="text-green-400 font-bold">15,000+ active users</span>, implementing JWT authentication, adaptive rate limiting, and fault isolation.</li>
                        <li>Developed real-time notification and messaging service using Redis Pub/Sub and WebSockets, supporting <span class="text-blue-400 font-bold">5,000+ concurrent connections</span> with sub-150ms latency.</li>
                        <li>Reduced infrastructure cost by <span class="text-green-400 font-bold">25%</span> (~$30K annually) through container resource profiling, right-sizing, and intelligent allocation.</li>
                        <li>Led decomposition of monolithic system into 6 independent service-oriented modules, reducing regression issues by <span class="text-green-400 font-bold">30%</span> and cutting post-release hotfixes from 8/month to under 3.</li>
                    </ul>
                ''',
                'date_start': 'Jul 2021',
                'date_end': 'Jun 2022',
                'technologies': 'Microservices, Node.js, JWT, Redis (Pub/Sub), WebSockets, Docker, REST APIs, RBAC',
                'order': 2,
            },

            # Projects
            {
                'category': 'project',
                'title': 'Detecting Humans in Fire',
                'subtitle': 'MSc Applied Research Project — Computer Vision AI Safety System',
                'description': '''
                    <p class="mb-3">Architected a dual-model computer vision system integrating <strong>EfficientNetB0</strong> (fire detection) and <strong>YOLOv8</strong> (human detection), producing a 4-state situational risk assessment for first responders.</p>
                    <ul class="list-disc list-inside space-y-1 text-sm text-gray-300 mb-3">
                        <li>90.9% fire detection accuracy / 98.1% precision (EfficientNetB0)</li>
                        <li>90.8% human detection accuracy / 99.6% precision (YOLOv8)</li>
                        <li>Deployed as Flask web app processing images fully in-memory for instant risk output</li>
                    </ul>
                    <p class="mt-3">
                        <a href="https://github.com/imyogeshgaikwad/Detecting-Humans-In-Fire" target="_blank"
                           class="text-blue-400 hover:underline text-sm">🔗 View on GitHub →</a>
                    </p>
                ''',
                'technologies': 'Python, TensorFlow, EfficientNetB0, YOLOv8, Flask, OpenCV',
                'order': 1,
            },
            {
                'category': 'project',
                'title': 'CAReader-Ai',
                'subtitle': 'AI-Powered Car Dealership Platform',
                'description': '''
                    <p class="mb-3">Full-stack car dealership management platform with <strong>Node.js</strong> backend and OpenAI API integration for an AI client communication layer — handling vehicle info generation, customer queries, and dealership workflows end-to-end.</p>
                    <p class="text-gray-400 text-sm mb-3">RESTful API backend covering full CRUD lifecycle for vehicle records, client profiles, and transaction history.</p>
                    <p class="mt-3">
                        <a href="https://github.com/imyogeshgaikwad/CAReader-Ai" target="_blank"
                           class="text-blue-400 hover:underline text-sm">🔗 View on GitHub →</a>
                    </p>
                ''',
                'technologies': 'Node.js, JavaScript, OpenAI API, REST APIs',
                'order': 2,
            },

            # Skills
            {
                'category': 'skill',
                'title': 'Languages',
                'subtitle': 'Programming Languages',
                'description': '''
                    <div class="flex flex-wrap gap-2">
                        <span class="px-3 py-1 bg-blue-600/30 rounded-full text-blue-300">JavaScript (Node.js)</span>
                        <span class="px-3 py-1 bg-blue-600/30 rounded-full text-blue-300">TypeScript</span>
                        <span class="px-3 py-1 bg-blue-600/30 rounded-full text-blue-300">Python</span>
                        <span class="px-3 py-1 bg-blue-600/30 rounded-full text-blue-300">Java</span>
                        <span class="px-3 py-1 bg-blue-600/30 rounded-full text-blue-300">SQL</span>
                        <span class="px-3 py-1 bg-blue-600/30 rounded-full text-blue-300">Bash</span>
                    </div>
                ''',
                'order': 1,
            },
            {
                'category': 'skill',
                'title': 'Backend Systems',
                'subtitle': 'Server-Side & Architecture',
                'description': '''
                    <div class="flex flex-wrap gap-2">
                        <span class="px-3 py-1 bg-blue-600/30 rounded-full text-blue-300">Microservices</span>
                        <span class="px-3 py-1 bg-blue-600/30 rounded-full text-blue-300">RESTful APIs</span>
                        <span class="px-3 py-1 bg-blue-600/30 rounded-full text-blue-300">Event-Driven Architecture</span>
                        <span class="px-3 py-1 bg-blue-600/30 rounded-full text-blue-300">Message Queues (Redis, SQS)</span>
                        <span class="px-3 py-1 bg-blue-600/30 rounded-full text-blue-300">WebSockets</span>
                        <span class="px-3 py-1 bg-blue-600/30 rounded-full text-blue-300">Background Job Processing</span>
                        <span class="px-3 py-1 bg-blue-600/30 rounded-full text-blue-300">Rate Limiting</span>
                        <span class="px-3 py-1 bg-blue-600/30 rounded-full text-blue-300">JWT / RBAC</span>
                    </div>
                ''',
                'order': 2,
            },
            {
                'category': 'skill',
                'title': 'Cloud & DevOps',
                'subtitle': 'Infrastructure & Tooling',
                'description': '''
                    <div class="flex flex-wrap gap-2">
                        <span class="px-3 py-1 bg-orange-600/30 rounded-full text-orange-300">AWS (EC2, S3, Lambda, RDS, CloudWatch, IAM, VPC)</span>
                        <span class="px-3 py-1 bg-orange-600/30 rounded-full text-orange-300">Docker</span>
                        <span class="px-3 py-1 bg-orange-600/30 rounded-full text-orange-300">Kubernetes</span>
                        <span class="px-3 py-1 bg-orange-600/30 rounded-full text-orange-300">CI/CD Pipelines</span>
                        <span class="px-3 py-1 bg-orange-600/30 rounded-full text-orange-300">GitHub Actions</span>
                        <span class="px-3 py-1 bg-orange-600/30 rounded-full text-orange-300">Infrastructure as Code</span>
                        <span class="px-3 py-1 bg-orange-600/30 rounded-full text-orange-300">Linux</span>
                    </div>
                ''',
                'order': 3,
            },
            {
                'category': 'skill',
                'title': 'Databases',
                'subtitle': 'Data Storage & Optimisation',
                'description': '''
                    <div class="flex flex-wrap gap-2">
                        <span class="px-3 py-1 bg-yellow-600/30 rounded-full text-yellow-300">PostgreSQL</span>
                        <span class="px-3 py-1 bg-yellow-600/30 rounded-full text-yellow-300">MongoDB</span>
                        <span class="px-3 py-1 bg-yellow-600/30 rounded-full text-yellow-300">Redis (Caching, Pub/Sub, Clustering)</span>
                        <span class="px-3 py-1 bg-yellow-600/30 rounded-full text-yellow-300">MySQL</span>
                        <span class="px-3 py-1 bg-yellow-600/30 rounded-full text-yellow-300">Query Optimisation</span>
                        <span class="px-3 py-1 bg-yellow-600/30 rounded-full text-yellow-300">Index Design</span>
                        <span class="px-3 py-1 bg-yellow-600/30 rounded-full text-yellow-300">Database Sharding</span>
                    </div>
                ''',
                'order': 4,
            },
            {
                'category': 'skill',
                'title': 'Architecture & Reliability',
                'subtitle': 'Distributed Systems & Observability',
                'description': '''
                    <div class="flex flex-wrap gap-2">
                        <span class="px-3 py-1 bg-purple-600/30 rounded-full text-purple-300">Distributed Systems</span>
                        <span class="px-3 py-1 bg-purple-600/30 rounded-full text-purple-300">Horizontal Scaling</span>
                        <span class="px-3 py-1 bg-purple-600/30 rounded-full text-purple-300">Load Balancing</span>
                        <span class="px-3 py-1 bg-purple-600/30 rounded-full text-purple-300">Fault Tolerance</span>
                        <span class="px-3 py-1 bg-purple-600/30 rounded-full text-purple-300">High Availability</span>
                        <span class="px-3 py-1 bg-purple-600/30 rounded-full text-purple-300">Monitoring (CloudWatch)</span>
                        <span class="px-3 py-1 bg-purple-600/30 rounded-full text-purple-300">Centralised Logging</span>
                        <span class="px-3 py-1 bg-purple-600/30 rounded-full text-purple-300">MTTR Optimisation</span>
                    </div>
                ''',
                'order': 5,
            },
            {
                'category': 'skill',
                'title': 'Frontend',
                'subtitle': 'UI & Web Technologies',
                'description': '''
                    <div class="flex flex-wrap gap-2">
                        <span class="px-3 py-1 bg-teal-600/30 rounded-full text-teal-300">React.js</span>
                        <span class="px-3 py-1 bg-teal-600/30 rounded-full text-teal-300">Redux</span>
                        <span class="px-3 py-1 bg-teal-600/30 rounded-full text-teal-300">Performance Optimisation</span>
                        <span class="px-3 py-1 bg-teal-600/30 rounded-full text-teal-300">Component Architecture</span>
                    </div>
                ''',
                'order': 6,
            },
        ]

        for item_data in items:
            PortfolioItem.objects.create(**item_data)

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {len(items)} portfolio items!'))