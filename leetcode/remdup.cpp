#include <iostream>
#include <unordered_map>
#include <functional>

constexpr int DEF_LIST_VAL = 0;

template <typename T>
class ListNode {
private:
    T val;
    ListNode<T>* prev;
    ListNode<T>* next;
public:
    ListNode(T val, ListNode<T>* prev, ListNode<T>* next): 
        val(val), prev(prev), next(next) {}
    ListNode(T val, ListNode<T>* prev): ListNode(val, prev, nullptr) {}
    ListNode(T val): ListNode(val, nullptr) {}
    ListNode(): ListNode(DEF_LIST_VAL) {}

    ListNode<T>* append(T a);
    ListNode<T>* rem_dup();
    void iter(std::function<void(T&)> it);
    void clear();
};

template <typename T>
ListNode<T>* ListNode<T>::append(T a) {
    ListNode<T>* cur = this;
    while(cur->next)
        cur = cur->next;
    
    ListNode<T>* new_node = new ListNode(a, cur);
    cur->next = new_node;
    return this;
}

template <typename T>
ListNode<T>* ListNode<T>::rem_dup() {
    std::unordered_map<T, int> dup_map;
    ListNode<T>* cur = this;

    while(cur) {
        if(dup_map[cur->val]) {
            cur->prev->next = cur->next;
            if(cur->next)
                cur->next->prev = cur->prev;
            
            ListNode<T>* dummy = cur;
            cur = cur->next;
            delete dummy;
            
        } else {
            dup_map[cur->val] = 1;
            cur = cur->next;
        }
    }
    return this;
}

template <typename T>
void ListNode<T>::clear() {
    ListNode<T>* cur = this->next;

    while(cur) {
        ListNode<T>* dummy = cur;
        delete dummy;
        cur = cur->next;
    }
}

template <typename T>
void ListNode<T>::iter(std::function<void(T&)> it) {
    ListNode<T>* cur = this;
    while(cur) {
        ListNode<T>* next = cur->next;
        it(cur->val);
        cur = next;
    }
}

int main() {
    ListNode<int>* list = new ListNode<int>(1);
    list
        ->append(2)
        ->append(3)
        ->append(2)
        ->append(3)
        ->append(3)
        ->append(4)
        ->append(1)
        ->rem_dup();
    list->iter([](int& i){ std::cout << i << std::endl; });
    list->clear();
    return 0;
}